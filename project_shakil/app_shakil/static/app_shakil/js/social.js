/*
Social Media share link

What'sapp share link:
https://api.whatsapp.com/send?text=[post-title] [post-url]

FacebooK:
https://www.facebook.com/sharer.php?u=[post-url]

social_share

*/

const SocialBtn = document.querySelector(".social_share_btn")

function init(){
    let postUrl = encodeURI(document.location.href);
    SocialBtn.setAttribute("href",`https://www.facebook.com/sharer.php?u=${postUrl}`)
}

init()