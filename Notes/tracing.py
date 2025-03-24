#Matthew McKinley Tracing Notes

#What is tracing?
    #debugging method that lets you see what is happening with your functions
# python -m trace --trace C:\Users\matthew.mckinley\Documents\CP2-Projects\Notes\tracing.py
"""
--trace (displays function lines as they are executed)
--count (displays the number of times each function is executed)
--listfuncs (displays the functions in the project)
--trackcalls (displays relationships between functions)
"""

#What are some ways we can debug by tracing?
    #make a function that lets us see how our functions are interacting and running
#How do you access the debugger in VS Code?
    #f5, debugging area in the left bar, press the dropdown with the play button
#What is testing?
    #
#What are boundary conditions?

#How do you handle when users give strange inputs?

import trace
import sys

tracer = trace.Trace(count=False, trace=True)
def trace_calls(frame, event, arg):
    if event == "call":
        print(f"Calling function: {frame.f_code.co_name}")
    elif event == "line":
        print(f"Executing line: {frame.f_lineno} in {frame.f_code.co_name}")
    elif event =="return":
        print(f"{frame.f_code.co_name} returned {arg}")
    elif event == "exception":
        print(f"Exception in {frame.f_code.co_name}: {arg}")
    return trace_calls

sys.settrace(trace_calls)

"""
Event types:
call - When the function is called
line - When a new line is executed
return - When the function returns a value
exception - When there is an exception raised
"""

def add(num_one, num_two):
    return num_one + num_two

def sub(num_one, num_two):
    return num_one - num_two

print(add(538, 463))
print(sub(538, 463))

#tracer.run("sub")