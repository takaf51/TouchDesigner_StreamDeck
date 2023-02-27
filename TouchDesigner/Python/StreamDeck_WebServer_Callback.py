# Http Request Handler
def onHTTPRequest(webServerDAT, request, response):
	response['statusCode'] = 200 # OK
	response['statusReason'] = 'OK'
	response['data'] = handle_command(request['uri'])
	return response

# Command handler: Dispatch command by URI
def handle_command(uri):
	switcher = {
		"/create_3d_ops": create_3d_ops,
		"/python_dev_pane": create_python_dev_pane,
		"/3d_dev_pane": create_3d_dev_pane,
		"/default_pane": default_pane,
		"/create_null_op": create_null_ops
	}
	func = switcher.get(uri, command_not_found)
	return func()


# Set Default Pane Layout
def default_pane():
	print(len(ui.panes))
	for idx in range(1, len(ui.panes)):
		ui.panes[idx].close()
	return "Deofault Pane Called"


# Set python dev pane Layout
def create_python_dev_pane():
	default_pane()
	root_pane = ui.panes[0]
	python_pane = root_pane.splitRight()
	root_pane.ratio = .8
	python_pane.changeType(PaneType.TEXTPORT)
	return "Python Dev Pane Called"


# Set 3D dev pane Layout
def create_3d_dev_pane():
	default_pane()
	root_pane = ui.panes[0]
	root_pane.showBackdropTOPs = False
	geo_pane = root_pane.splitRight()
	geo_pane.ratio = .2
	geo_pane = geo_pane.changeType(PaneType.GEOMETRYVIEWER)
	top_pane = geo_pane.splitBottom()
	top_pane = top_pane.changeType(PaneType.TOPVIEWER)
	return "3D Pane Called"
	
# Create null operator
def create_null_ops():
	nulls = {
		'COMP': nullCOMP, 
		'TOP': nullTOP, 
		'CHOP': nullCHOP,
		'SOP': nullSOP,
		'MAT': nullMAT,
		'DAT': nullDAT
	}
	s = ui.messageBox('Create Null', 'Type?', buttons=list(nulls.keys()))
	op = parent().create(list(nulls.values())[s])
	op.nodeCenterX = ui.panes[0].x
	op.nodeCenterY = ui.panes[0].y
	op.viewer = True
	return "Create null operator Called"


# Create operators for 3D rendering
def create_3d_ops():
	xMergin = 300
	yMergin = -200
	cX = ui.panes[0].x
	cY = ui.panes[0].y
	operators = [geometryCOMP, renderTOP, outTOP, cameraCOMP, lightCOMP]
	nodes = {}
	for idx, op in enumerate(operators, start=0):
		node = parent().create(op)
		node.nodeCenterX = (idx % 3) * xMergin + cX
		node.nodeCenterY = (idx // 3) * -yMergin + cY
		node.viewer = True
		nodes[op] = node
	[op.destroy() for op in nodes[geometryCOMP].ops("*")]
	inOP = nodes[geometryCOMP].create(inSOP)
	outOP = nodes[geometryCOMP].create(outSOP)
	inOP.outputConnectors[0].connect(outOP)
	outOP.nodeCenterX += xMergin
	outOP.display = True
	outOP.render = True
	nodes[outTOP].display = True
	nodes[renderTOP].outputConnectors[0].connect(nodes[outTOP])
	return "Create 3D Called"
	

# Command not found
def command_not_found():
	print("Unknown command was requested")
	return "Command Not Found"
