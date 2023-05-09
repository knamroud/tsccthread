# TSCCThread
This repository contains a simple Python class implementing a Thread to compile and debug TypeScript files at runtime in a Django or Flask project.  
## Usage
Run the thread passing the "input" (TypeScript) and "output" (JavaScript) directory.  
You can specify additional flags for the tsc as third parameter. Please, do pass them as a string.   
The fourth parameter is a debug flag. If True, the thread will keep running and checking for file edits, otherwise it will only run one time.  
Please not that any file not ending in .ts or starting with a . contained in the input directory will be deleted.  
When running with Flask in debug mode, add `from werkzeug.serving import is_running_from_reloader` at the top of your file and run the thread in an `if not is_running_from_reloader():`. This will avoid the thread restarting every time the server restarts.  
## Examples
Run the thread in your main code:  
```bash
ts_check = TSCCThread("static/ts", "static/js")
ts_check.start()```
