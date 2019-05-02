<span style="font-family:SimSun;font-size:14px;">@ECHO OFF
TITLE BAT脚本例子3
COLOR A
echo -----------BAT脚本例子3-----------
echo=
echo=
TYPE tree_list1.txt
rem 复制（合并）文件 /Y 表示目标路径存在该文件则不提示直接覆盖
COPY /Y tree_list2.txt + tree_list3.txt C:\
 
DEL tree_list4.txt /f /s /q /a 
rem /f 表示强制删除文件 
rem /s表示子目录都要删除该文件 
rem /q表示无声，不提示 
rem /a根据属性选择要删除的文件 
 
rem 需要特别注意的是：move不能跨分区移动文件夹
MOVE example3 example3_1
echo=
echo=
echo --------------------------------------------
PAUSE</span>