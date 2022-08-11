import pyml

# system models
system_name = "Battle Simulator"
actors = ['Battle Planner']
use_cases = ['Simulate Battle']
interactions = [('Battle Planner', 'Simulate Battle')]
use_case_relationships = []

objects = ['main']
actions = [
('Battle Planner', 'main', 'run()'),
('main', 'Battle Planner', 'request for side 1 starting level'),
('Battle Planner', 'main', 'side 1 starting level'),
('main', 'Battle Planner', 'request for side 1 lethality coefficient'),
('Battle Planner', 'main', 'side 1 lethality coefficient'),
('main', 'Battle Planner', 'request for side 2 starting level'),
('Battle Planner', 'main', 'side 2 starting level'),
('main', 'Battle Planner', 'request for side 2 lethality coefficient'),
('Battle Planner', 'main', 'side 2 lethality coefficient'),
('main', 'Battle Planner', 'time history of troops'),
]

# create diagrams
pyml.use_case_diagram(system_name, actors, use_cases, interactions, use_case_relationships, filename=system_name+' Use Case Diagram', format='pdf')
pyml.sequence_diagram(system_name, actors, objects, actions, filename=system_name+" Sequence Diagram", format='pdf')
