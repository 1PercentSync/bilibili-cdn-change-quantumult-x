// bilibili_cdn_change.js
const targetCDN = "upos-hz-mirrorakam.akamaized.net";

// 处理请求头
function changeCDNHeader(request) {
    const url = new URL(request.url);
    const isBiliBiliVideo = /^https:\/\/[a-z.-\d]*(bilivideo.com|akamaized.net)/i.test(url);
    if (isBiliBiliVideo) {
        url.host = targetCDN;
        request.url = url.href;
    }
    return request;
}

// Quantumult X的回调函数
$done(changeCDNHeader($request));
