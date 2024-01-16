# bilibili cdn change quantumult x
 a Quantumult X rewrite script to change Bilibili's CDN(by default, use Akamai)
一个Quan X（圈X/QuanX）脚本用于切换哔哩哔哩所使用的CDN，默认切换为Akamai
使用方法：
添加重写引用资源：
https://github.com/1PercentSync/bilibili-cdn-change-quantumult-x/raw/main/bilibili_cdn_change.conf
确保开启MITM
切换到Akamai以外的CDN，请下载修改js中的：
const targetCDN = "upos-hz-mirrorakam.akamaized.net";
为其他地址，包括但不限于：
upos-sz-mirrorks3.bilivideo.com
upos-sz-mirrorks3b.bilivideo.com
upos-sz-mirrorks3c.bilivideo.com
upos-sz-mirrorks32.bilivideo.com
upos-sz-mirrorcos.bilivideo.com
upos-sz-mirrorcosb.bilivideo.com
upos-sz-mirrorbos.bilivideo.com
upos-sz-mirrorhw.bilivideo.com
upos-sz-mirrorhwb.bilivideo.com
upos-sz-upcdnbda2.bilivideo.com
upos-sz-upcdnws.bilivideo.com
upos-sz-upcdnhw.bilivideo.com
upos-tf-all-js.bilivideo.com
cn-hk-eq-bcache-01.bilivideo.com
upos-hz-mirrorakam.akamaized.net
upos-sz-mirrorali.bilivideo.com
upos-sz-mirroraliov.bilivideo.com
upos-sz-mirror08h.bilivideo.com
