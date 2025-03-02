# chat_with_ai
DeepSeek 恢复正常后，便尝试编写一个MCDR插件，使MC服务器能够接入DeepSeek。

使用了openai库，理论上支持openai的模型均可使用此插件对接

文章地址：https://blog.gubaiovo.com/posts/ec277bd3.html

## 使用方法

扔进plugins文件夹，然后`!!MCDR plugin reload chat_with_ai`



## Command

`!!dsp help`: 查看帮助

`!!dsp history`: 查看历史消息

`!!dsp clear`: 清空历史消息

`!!dsp system`: 查看ai预设

`!!dsp system <system>`: 设置ai预设

`!!dsp prefix`: 查看ai名称

`!!dsp prefix <prefix>`: 设置ai名称

`!!dsp init system`: 初始化角色预设

`!!dsp init prefix`: 初始化角色预设

`!!dsp init all`: 全部初始化且清空历史记录

`!!dsp <message>`: 与AI对话



## 鸣谢

感谢22年的自己

> 世界生成算法吞下了我的十七岁。
>
> 那封没寄出的信还在末地折跃门边缘，
>
> 漂浮如未完成的红石电路。
>
> 当第一个AI村民说出预设外的对白，
>
> 我忽然听见2022年的自己，
>
> 在矿洞深处敲打铁轨的节奏。
>
> 那些被放弃的坐标参数，
>
> 正在基岩层下重新编译春天。
