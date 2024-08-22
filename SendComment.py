import WebSend
import GetPostId
import Config


TargetUrl = 'https://blog.qrasa.cn/msgb/'
PostId = GetPostId.Get('Apple很可能在iPhone16上使用2TB存储')

print(PostId)