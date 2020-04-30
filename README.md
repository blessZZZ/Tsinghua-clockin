# Tsinghua-clockin
本程序是基于python制作的清华[日报]学生健康与出行情况的每日打卡小程序，原理是利用selenium.webdriver库中的一些函数在浏览器上完成打卡过程的一系列操作。
<br/>可以通过windows系统配置让程序每日定时运行，来达到自动打卡的效果（辅导员再也不用担心我不签到啦！）


# 1.本地运行需要配备的环境

firefox浏览器（本人运行的版本是: 75.0，或其他版本)
<br/><br/>选用firefox浏览器的<strong>原因</strong>：~~因为作者懒~~......咳咳，因为其他浏览器不方便！()
<br/>例如win10自带的<strong>Edge</strong>浏览器，1.8版本以上的<strong>Edge</strong>浏览器运行selenium.webdriver需要在系统选项中开启开发者模式，对于一些人来说非常不方便。
<br/>而<strong>Chrome</strong>浏览器版本更新速度快，容易导致该程序失效

<br/>因此，建议下载firefox浏览器！

# 2.Firefox下载好了，接下来我要怎么做呢？
首先下载好我们的程序：
![image](https://github.com/blessZZZ/Tsinghua-clockin/blob/master/images/1.jpg))
<br/>点击Clone or download，然后下载zip版本，解压后我们可以得到：

<br/>其实只需要clickin.exe这个程序就行了，你可以直接运行一下看看效果:

<br/>(注意！360这时可能会出来加戏，你可以选择添加信任或者关掉360)
<br/>输入你的学号和密码，之后按回车键就可以自动运行了。这个程序只要输入过一次学号和密码，之后再启动时就不需要输入了。你会发现在clickin.exe的文件夹里多了一个txt文件:number.txt
<br/>这里面存放的就是你的学号与密码，如果你在未来修改了密码，可以在number.txt里直接编辑

# 3.我要怎么让这个程序每天自动运行呢？
这里我用的是win10系统，如果你是mac系统和linux系统，系统里也是有自动执行程序的方法的。

首先，我们要按住win+R键，在打开的运行窗口中输入命令control schedtasks
<br/>电脑会打卡如下界面：

<br/>点击"操作"-->"创建基本任务"

<br/>接下来的操作如图所示:
<br/>你可以自己选择启动的时间和启动的间隔
<br/>这里的路径选择的你下载的clockin.exe的位置，选择它

<br/>点击完成，之后程序就会按时自动运行了
