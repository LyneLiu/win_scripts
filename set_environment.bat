::批处理环境变量
@echo off
set /p sublime_text=please input:
echo %sublime_text%
echo %path%

setx PATH "%PATH%;%sublime_text%" /m

echo %path%
pause