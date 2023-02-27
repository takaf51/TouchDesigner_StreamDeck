# td_streamdeck
<p align="center"><img width="50%" src="Icons/TD_SD.png" /></p>

**This is a setup for operating TouchDesigner with StreamDeck. For some functions that cannot be achieved with keyboard shortcuts, I use TouchDesigner's WebServer to call the URI corresponding to the Python function implemented in the WebServerOP via http from StreamDeck.　Both Stream Deck and TouchDesigner require configuration.**

## Stream Deck
**Please import the DeckProfile. You also need to install the API Ninja and Super Macro plugins. Please adjust the server address, port number, etc. according to your environment.**

## TouchDesigner
**Please use the tox file in this repository as is, or set it as the Custom Startup File by going to Preferences -> General -> Start Up File and changing it to "Custom File" and specifying the Custom Startup File.**

**If you need to modify or add functions, please add the URI and function name to the "switcher" dictionary in the Python script of the Web Server DAT OP (StreamdeckCommandReceiver), and add the function accordingly.**


| Icon        | Function           | Equivalente Shortcut  |
| :-------------: |:-------------| :-----:|
| <img alt='TD' width='57' src='Icons/TD_Logo.png'/>| Default Pane Layout  | Call Python API (http) |
| <img alt='TD' width='57' src='Icons/3Ddev.png'/>| Pane Layout for Python Dev  | Call Python API (http) |
| <img alt='TD' width='57' src='Icons/PythonDev.png'/>| Pane Layout for 3D  | Call Python API (http) |
| <img alt='TD' width='57' src='Icons/3D.png'/>| Create OPs for Rendering  | Call Python API (http) |
| <img alt='TD' width='57' src='Icons/NextPage.png'/>| Next Page  | Stream Deck Function |
| <img alt='TD' width='57' src='Icons/parameter.png'/>| Parameter Show / Hide | P |
| <img alt='TD' width='57' src='Icons/Preview.png'/>| Perform Mode Enter  | F1 |
| <img alt='TD' width='57' src='Icons/View.png'/>| Open Current Op Viewer  | Shift + V |
| <img alt='TD' width='57' src='Icons/Null.png'/>| Create null OP  | Call Python API (http) |
| <img alt='TD' width='57' src='Icons/BS.png'/>| Delete Selection  | Backspace |
| <img alt='TD' width='57' src='cons/PlayPause.png'/>| Play / Pause  | SPACE |
| <img alt='TD' width='57' src='Icons/Home.png'/>| Home All  | H |
| <img alt='TD' width='57' src='Icons/Bypass.png'/>| Bypass OP  | B |
| <img alt='TD' width='57' src='Icons/Undo.png'/>| Undo  | Ctrl + Z |
| <img alt='TD' width='57' src='Icons/CreateNewOperator.png'/>| Create OP by Voice Typing  | Double Click, Win + H (Windows Only)  |
