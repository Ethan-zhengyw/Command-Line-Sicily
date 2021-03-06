Command Line Sicily
===================

This little project help you to submit your source code to soj.me and get the response you need by using terminal commands

Overview
------------------------
### Why do I do this job
Our school has a online check system[http://soj.me] for our source code, and every time after finishing my code, I have to...
    
    1.open a browser
    2.login to soj.me
    3.find the problem and click it
    4.click submit button
    5.copy my source code
    6.past into the code box of the webpage
    7.if don't pass the test, maybe have to repeat some steps again and again 
      
  OMG, I can submit my code by now!!!(一两次就Accepted的学霸大牛除外)
  How can I endure such a situation? So I decided to simplify the process to submit by finished that in commands line.
### Basic Functions

  - submit source code to soj.me

	```python
	sudo python ./main.py [problem_ID] [path_to_your_sourcefile]
	```
  	![image](https://raw.githubusercontent.com/Ethan-zhengyw/Sicily-Online-Judge/master/screenshots/Accepted.png)
	  
  - retrieve a problem
	```python
      	sudo python ./retrieve.py [problem_ID]
	```
  	![image](https://raw.githubusercontent.com/Ethan-zhengyw/Sicily-Online-Judge/master/screenshots/retrieve-problem.png)

### Quick Start
      
  - Download this repository
        
        sudo git clone git://github.com/Ethan-zhengyw/Command-Line-Sicily.git
  
  - Decompressed and now you get a folder Sicily-Online-Judge which contains only three .py files.
        
    If you want to submit code please edit file ./sicily/soj.conf: replace USERNAME and PASSWORD with your own information
    content of file soj.conf after your modify should be:

        USERNAME = [this_is_your_username]
        PASSWORD = [this_is_your_password]
    
  - Submit your code and get the result
      
        sudo python main.py [problem_ID] [path_to_your_sourcefile]

  - retrieve detail information of a certain problem

	sudo python retrieve.py [problem_ID]
	
### Extra Info for Vimer
If you are programming with vim, then there is a much cool way to submit your code for you.

All you have to do is the following things
  
  - get this repository's folder and place it in anywhere you want
  - modify ./sicily/soj.conf and put it into the same directory with your source code file
  - add these code into your vimrc file (Do replace content between '' with your main.py path)

	```vimscript  
    let g:PATH_SICILY_MAINPY='/home/zheng/文档/sicily/main.py'
    let g:PATH_SICILY_RETRIEVEPY='/home/zheng/文档/sicily/retrieve.py'
	command! -nargs=1 Sicily call s:Run_Sicily_Judge(<f-args>)
	func! s:Run_Sicily_Judge(problemId)
	    let a:filename = expand('%')
		exec ":! clear"
		exec ":! sudo python " . g:PATH_SICILY_MAINPY . " " . a:problemId . " " . a:filename
	endfunc
	command! -nargs=1 Sicilyquery call s:Run_Sicily_Query(<f-args>)
	func! s:Run_Sicily_Query(problemId)
	    let a:filename = expand('%')
		exec ":! clear"
		exec ":! sudo python " . g:PATH_SICILY_RETRIEVEPY . " " . a:problemId
	endfunc
	```

  
  - When editing a cpp file, you can submit your code by execute
  
        :Sicily [problemId]

      For example
        
        :Sicily 1151
        
      will submit the code of the current file you are editing to soj.me and then display the result in this way:
      
         Problem Info
        +----------------------------
         [1151. 魔板]
         [Time Limit: 1 secs]  [Memory Limit: 32 MB]

         Waiting...
         Judging...

         Result
        +----------------------------
         Status:     [Accepted]
         Run Memory: [3216KB]
         Run Time:   [0.09secs]
         
     
      Display the detail information of problem 1151
 
	    :Sicilyquery 1151
	
### Todo
  - query a problem by it's ID and display it in a pretty way [solved]
  - support more detail information when didn't receive a "Accepted" result [solved]
 
