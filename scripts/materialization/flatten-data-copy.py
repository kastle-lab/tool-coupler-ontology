import json
import csv
import os

def extract_hierarchy_pairs(prop_dict, parent_name, server_name, tool_name, parameter_name, element_data_types, hierarchy_data_types):
    """
    Recursively extract parent-child element pairs and parameter-to-element linkages.
    """
    param_element_rows = []
    hierarchy_rows = []
    
    for prop_name, prop_data in prop_dict.items():
        raw_type = prop_data.get('type', 'string')
        if isinstance(raw_type, list):
            raw_type = raw_type[0] if raw_type else 'string'
        data_type = str(raw_type).capitalize()
        description = prop_data.get('description', '')

        if not parent_name:
            # Top-level item directly under the parameter
            element_data_types.add(data_type)
            param_element_rows.append({
                'server_name': server_name,
                'tool_name': tool_name,
                'parameter_name': parameter_name,
                'element_name': prop_name,
                data_type: data_type,
                'element_description': description
            })
        else:
            # Nested child item belonging to a parent element
            hierarchy_data_types.add(data_type)
            hierarchy_rows.append({
                'server_name': server_name,
                'tool_name': tool_name,
                'parameter_name': parameter_name,
                'parent_element_name': parent_name,
                'child_element_name': prop_name,
                data_type: data_type,
                'element_element_description': description
            })
            
        # Check for deeper nested properties inside objects or arrays
        nested_props = {}
        if 'properties' in prop_data:
            nested_props = prop_data['properties']
        elif 'items' in prop_data and isinstance(prop_data['items'], dict) and 'properties' in prop_data['items']:
            nested_props = prop_data['items']['properties']
            
        if nested_props:
            sub_params, sub_hierarchy = extract_hierarchy_pairs(
                prop_dict=nested_props,
                parent_name=prop_name,
                server_name=server_name,
                tool_name=tool_name,
                parameter_name=parameter_name,
                element_data_types=element_data_types,
                hierarchy_data_types=hierarchy_data_types
            )
            param_element_rows.extend(sub_params)
            hierarchy_rows.extend(sub_hierarchy)
            
    return param_element_rows, hierarchy_rows

def flatten_data():
    # --- Dynamic Directory Resolution ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    if os.path.exists(os.path.join(script_dir, 'list-tools.json')):
        data_dir = script_dir
    elif os.path.exists(os.path.join(script_dir, 'data', 'list-tools.json')):
        data_dir = os.path.join(script_dir, 'data')
    elif os.path.exists(os.path.join(script_dir, '..', 'data', 'list-tools.json')):
        data_dir = os.path.join(script_dir, '..', 'data')
    else:
        data_dir = os.getcwd() 
    
    print(f"Using data directory: {data_dir}")
    
    list_tools_path = os.path.join(data_dir, 'list-tools.json')
    server_tools_path = os.path.join(data_dir, 'server-tools.txt')
    
    out_tools_path = os.path.join(data_dir, 'tools.csv')
    out_servers_path = os.path.join(data_dir, 'servers.csv')
    out_params_path = os.path.join(data_dir, 'parameters.csv')
    out_params_elements_path = os.path.join(data_dir, 'parameters-to-elements.csv')
    out_hierarchy_path = os.path.join(data_dir, 'elements-hierarchy.csv')
    # ------------------------------------

    # Map servers to tools FIRST so we can add server_name to everything
    print("Parsing server-tools.txt...")
    tool_to_server = {}
    server_rows = []
    current_server = ""
    
    if os.path.exists(server_tools_path):
        with open(server_tools_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.endswith('tools):'):
                    current_server = line.split(' ')[0]
                elif line.startswith('- '):
                    t_name = line[2:].strip()
                    tool_to_server[t_name] = current_server
                    server_rows.append({
                        'server_name': current_server, 
                        'tool_name': t_name
                    })
    else:
        print(f"Warning: server-tools.txt not found at {server_tools_path}. Skipping server mappings.")

    print("Parsing list-tools.json...")
    with open(list_tools_path, 'r', encoding='utf-8') as f:
        tools_data = json.load(f)

    tools_rows = []
    param_rows = []
    all_param_elements = []
    all_hierarchy = []
    
    # Store dynamic data types for headers
    param_data_types = set()
    element_data_types = set()
    hierarchy_data_types = set()

    for tool in tools_data:
        tool_name = tool.get('name', '')
        server_name = tool_to_server.get(tool_name, '')
        
        tools_rows.append({
            'server_name': server_name,
            'tool_name': tool_name,
            'tool_description': tool.get('description', '') or ''
        })
        
        input_schema = tool.get('inputSchema') or {}
        output_schema = tool.get('outputSchema') or {}
        
        in_props = input_schema.get('properties', {}) if isinstance(input_schema.get('properties'), dict) else {}
        out_props = output_schema.get('properties', {}) if isinstance(output_schema.get('properties'), dict) else {}
        
        in_req = input_schema.get('required', []) if isinstance(input_schema.get('required'), list) else []
        out_req = output_schema.get('required', []) if isinstance(output_schema.get('required'), list) else []
        
        all_param_names = set(in_props.keys()).union(set(out_props.keys()))
        
        for p_name in all_param_names:
            in_schema_val = 'Input' if p_name in in_props else ''
            out_schema_val = 'Output' if p_name in out_props else ''
            
            p_data = in_props.get(p_name) or out_props.get(p_name) or {}
            is_req = 1 if (p_name in in_req or p_name in out_req) else 0
            
            raw_type = p_data.get('type', 'string')
            if isinstance(raw_type, list):
                raw_type = raw_type[0] if raw_type else 'string'
            p_type = str(raw_type).capitalize()
            p_desc = p_data.get('description', '')
            
            param_data_types.add(p_type)
            
            # 1. Capture ALL root parameters (primitives and complex objects alike)
            param_rows.append({
                'server_name': server_name,
                'tool_name': tool_name,
                'parameter_name': p_name,
                'input_schema': in_schema_val,
                'output_schema': out_schema_val,
                p_type: p_type,
                'parameter_description': p_desc,
                'is_required': is_req
            })
            
            # 2. Check for nested properties to extract elements
            nested_props = {}
            if 'properties' in p_data:
                nested_props = p_data['properties']
            elif 'items' in p_data and isinstance(p_data['items'], dict) and 'properties' in p_data['items']:
                nested_props = p_data['items']['properties']
                
            if nested_props:
                p_elements, p_hierarchy = extract_hierarchy_pairs(
                    prop_dict=nested_props,
                    parent_name="",
                    server_name=server_name,
                    tool_name=tool_name,
                    parameter_name=p_name,
                    element_data_types=element_data_types,
                    hierarchy_data_types=hierarchy_data_types
                )
                all_param_elements.extend(p_elements)
                all_hierarchy.extend(p_hierarchy)

    print("Writing decoupled CSV files...")
    
    with open(out_tools_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['server_name', 'tool_name', 'tool_description'])
        writer.writeheader()
        writer.writerows(tools_rows)
        
    with open(out_servers_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['server_name', 'tool_name'])
        writer.writeheader()
        writer.writerows(server_rows)
        
    with open(out_params_path, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['server_name', 'tool_name', 'parameter_name', 'input_schema', 'output_schema'] + sorted(list(param_data_types)) + ['parameter_description', 'is_required']
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval='')
        writer.writeheader()
        writer.writerows(param_rows)
        
    with open(out_params_elements_path, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['server_name', 'tool_name', 'parameter_name', 'element_name'] + sorted(list(element_data_types)) + ['element_description']
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval='')
        writer.writeheader()
        writer.writerows(all_param_elements)
        
    with open(out_hierarchy_path, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['server_name', 'tool_name', 'parameter_name', 'parent_element_name', 'child_element_name'] + sorted(list(hierarchy_data_types)) + ['element_element_description']
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval='')
        writer.writeheader()
        writer.writerows(all_hierarchy)

    print(f"Success! Generated files (tools.csv, servers.csv, parameters.csv, parameters_to_elements.csv, elements_hierarchy.csv) in {data_dir}")

if __name__ == "__main__":
    flatten_data()