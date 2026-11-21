# Tool hasToolGoal ToolGoal
disjoint: `Tool DisjointWith ToolGoal`

existential: `Tool SubClassOf hasToolGoal some ToolGoal`

global domain: `hasToolGoal some owl:Thing SubClassOf Tool`

global range: `owl:Thing SubClassOf hasToolGoal only ToolGoal`

qualified scoped functionality: `Tool SubClassOf hasToolGoal max 1 ToolGoal`

# Retrieval SubClassOf ToolGoal
subclass: `Retrieval SubClassOf ToolGoal`

# Search SubClassOf Retrieval
subclass: `Search SubClassOf Retrieval`

# Acquisition SubClassOf Retrieval
subclass: `Acquisition SubClassOf Retrieval`

# Analysis subClassOf ToolGoal
subclass: `Analysis SubClassOf ToolGoal`

# Filtering SubClassOf Analysis
subclass: `Filtering SubClassOf Analysis`

# Sorting SubClassOf Analysis
subclass: `Sorting SubClassOf Analysis`

# Rank SubClassOf Sorting
subclass: `Rank SubClassOf Sorting`

# Alphanumeric SubClassOf Sorting
subclass: `Alphanumeric SubClassOf Sorting`

# Numeric SubClassOf Sorting
subclass: `Numeric SubClassOf Sorting`

# Alphabetic SubClassOf Sorting
subclass: `Alphabetic SubClassOf Sorting`

# Examination SubClassOf Analysis
subclass: `Examination SubClassOf Analysis`

# Verification SubClassOf Examination
subclass: `Verification SubClassOf Examination`

# Comparison SubClassOf Examination
subclass: `Comparison SubClassOf Examination`

# Transformation SubClassOf ToolGoal
subclass: `Transformation SubClassOf ToolGoal`

# Calculation SubClassOf Transformation
subclass: `Calculation SubClassOf Transformation`

# Conversion SubClassOf Transformation
subclass: `Conversion SubClassOf Transformation`

# Value SubClassOf Conversion
subclass: `Value SubClassOf Conversion`

# Representation SubClassOf Conversion
subclass: `Representation SubClassOf Conversion`

# Update SubClassOf Transformation
subclass: `Update SubClassOf Transformation`

# Additon SubClassOf Update
subclass: `Additon SubClassOf Update`

# Modification SubClassOf Update
subclass: `Modification SubClassOf Update`

# Removal SubClassOf Update
subclass: `Removal SubClassOf Update`

# Deletion SubClassOf Removal
subclass: `Deletion SubClassOf Removal`

# Clearing SubClassOf Removal
subclass: `Clearing SubClassOf Removal`

# Generation SubClassOf ToolGoal
subclass: `Generation SubClassOf ToolGoal`

# Execution SubClassOf ToolGoal
subclass: `Execution SubClassOf ToolGoal`

# Inaction SubClassOf ToolGoal
subclass: `Inaction SubClassOf ToolGoal`

# Simulation SubClassOf ToolGoal
subclass: `Simulation SubClassOf ToolGoal`

