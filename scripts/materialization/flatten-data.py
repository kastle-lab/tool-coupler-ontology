import json
import csv
import os

def flatten_data():
    # ---------------------------------------------------------
    # 1. Parse list-tools.json
    # ---------------------------------------------------------
    print("Parsing list-tools.json...")
    with open('/home/mechree/repos/mcp-kg/scripts/data/list-tools.json', 'r', encoding='utf-8') as f:
        tools_data = json.load(f)

    tools_rows = []
    params_rows = []

    for tool in tools_data:
        tool_name = tool.get('name', '')
        tools_rows.append({
            'tool_name': tool_name,
            'tool_description': tool.get('description', '') or ''
        })
        
        # Safely extract input and output schemas
        input_schema = tool.get('inputSchema') or {}
        output_schema = tool.get('outputSchema') or {}
        
        in_props = input_schema.get('properties', {}) if isinstance(input_schema.get('properties'), dict) else {}
        out_props = output_schema.get('properties', {}) if isinstance(output_schema.get('properties'), dict) else {}
        
        in_req = input_schema.get('required', []) if isinstance(input_schema.get('required'), list) else []
        out_req = output_schema.get('required', []) if isinstance(output_schema.get('required'), list) else []
        
        # Get all unique parameter names from both schemas
        all_param_names = set(in_props.keys()).union(set(out_props.keys()))
        
        for p_name in all_param_names:
            # Determine if it's Input, Output, or Inout
            if p_name in in_props and p_name in out_props:
                schema_type = "Inout"
            elif p_name in in_props:
                schema_type = "Input"
            else:
                schema_type = "Output"
            
            # Pull data from the appropriate schema (defaulting to input if it's Inout)
            p_data = in_props.get(p_name) or out_props.get(p_name) or {}
            is_req = 1 if (p_name in in_req or p_name in out_req) else 0
            
            # Handle types (sometimes type is a list like ["string", "null"] in JSON schema)
            raw_type = p_data.get('type', 'string')
            if isinstance(raw_type, list):
                raw_type = raw_type[0] if raw_type else 'string'
                
            # Capitalize datatype to match ontology instances (e.g. string -> String)
            p_type = str(raw_type).capitalize() 
            p_desc = p_data.get('description', '')
            
            # Check for nested items (Elements)
            items_data = p_data.get('items', {})
            items_props = items_data.get('properties', {}) if isinstance(items_data, dict) else {}
            
            if not items_props:
                # No nested elements
                params_rows.append({
                    'tool_name': tool_name, 
                    'param_name': p_name, 
                    'schema_type': schema_type,
                    'data_type': p_type, 
                    'description': p_desc, 
                    'is_required': is_req,
                    'element_name': '', 
                    'element_type': '', 
                    'element_description': ''
                })
            else:
                # Iterate through nested elements
                for e_name, e_data in items_props.items():
                    e_raw_type = e_data.get('type', 'string')
                    if isinstance(e_raw_type, list):
                        e_raw_type = e_raw_type[0] if e_raw_type else 'string'
                        
                    e_type = str(e_raw_type).capitalize()
                    params_rows.append({
                        'tool_name': tool_name, 
                        'param_name': p_name, 
                        'schema_type': schema_type,
                        'data_type': p_type, 
                        'description': p_desc, 
                        'is_required': is_req,
                        'element_name': e_name, 
                        'element_type': e_type, 
                        'element_description': e_data.get('description', '')
                    })

    # ---------------------------------------------------------
    # 2. Parse server-tools.txt
    # ---------------------------------------------------------
    print("Parsing server-tools.txt...")
    server_rows = []
    current_server = ""
    
    if os.path.exists('/home/mechree/repos/mcp-kg/scripts/data/server-tools.txt'):
        with open('/home/mechree/repos/mcp-kg/scripts/data/server-tools.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.endswith('tools):'):
                    # Extract server name before the space (e.g., "airtable (12 tools):" -> "airtable")
                    current_server = line.split(' ')[0]
                elif line.startswith('- '):
                    # Extract tool name after the hyphen
                    server_rows.append({
                        'server_name': current_server, 
                        'tool_name': line[2:].strip()
                    })
    else:
        print("Warning: server-tools.txt not found. Skipping server mappings.")

    # ---------------------------------------------------------
    # 3. Write data to CSVs
    # ---------------------------------------------------------
    print("Writing flat data to CSVs...")
    
    # Write tools.csv
    with open('/home/mechree/repos/mcp-kg/scripts/data/tools.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['tool_name', 'tool_description'])
        writer.writeheader()
        writer.writerows(tools_rows)
        
    # Write parameters.csv
    with open('/home/mechree/repos/mcp-kg/scripts/data/parameters.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'tool_name', 'param_name', 'schema_type', 'data_type', 
            'description', 'is_required', 'element_name', 
            'element_type', 'element_description'
        ])
        writer.writeheader()
        writer.writerows(params_rows)
        
    # Write servers.csv
    with open('/home/mechree/repos/mcp-kg/scripts/data/servers.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['server_name', 'tool_name'])
        writer.writeheader()
        writer.writerows(server_rows)

    print("Success! Flattened CSV files generated: tools.csv, parameters.csv, servers.csv.")

if __name__ == "__main__":
    flatten_data()