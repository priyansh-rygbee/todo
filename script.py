import todoist
api = todoist.TodoistAPI('fc44bdb20cb968561390c39d85d3904c33f265d3')
api.sync(resource_types=['all'])