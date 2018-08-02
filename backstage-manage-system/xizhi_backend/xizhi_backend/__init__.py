# from .models import *
let code = ''
if(localStorage.AppType === 1){ // 分销
code = '02'
}else if(localStorage.AppType === 2){ //代理
code = '01'
}

    let param = {
    platFormCode:code
}