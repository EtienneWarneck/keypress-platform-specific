# keypress-platform-specific



**Detecting any single key pressed (without the input() need for Enter) from Python requires platform specific modules.**

We're using try/except to attempt to use the Windows module mscvcrt first.
If the system isn't Windows, we throw an exception (an error being silenced explicitely) to execute the code for Mac or Linux with the tty , termios and sys modules.

From Pluralsight videos : 
https://app.pluralsight.com/course-player?clipId=e0791635-ed0a-4352-9216-7173cdd61ea5