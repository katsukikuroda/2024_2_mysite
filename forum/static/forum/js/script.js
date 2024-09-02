// "use strict";

// //window.alert("Hello");

// // const num = window.prompt("半角整数を入力");

// // if(num%2 === 0){
// //     window.alert("偶数です");
// //     num = 3;
// // }else if(num%2 === 1){
// //     window.alert("奇数です");
// // }else{
// //     window.alert("半角整数を入力してください");
// // }

// // for(let i=5; i>0; i--){
// //     window.alert(i);
// // }

// const num = window.prompt("半角数字を入力");

// function Kawase(doller){
//     const yen = doller * 150;
//     return yen;
// }

// window.alert(num + "ドルは日本円で" + Kawase(num) + "です");


"use strict";

function change1(){
    window.alert("Hello");
}

hello.onclick = change1;

function change2(){
    const str = window.prompt("入力してください");
    window.alert(str);
}

shows.onclick = change2;


function levelup(){
    for(let i=1;i<=9;i++){
        // window.alert("レベルは"+i+"です");
        window.alert(`レベルは${i}です`);
    }
}

up.onclick = levelup;

function randoms(){
    const random = Math.floor(Math.random() * 10);
    if(random<=5){
        window.alert("N");
    }else if(random<=8){
        window.alert("✨R");
    }else{
        window.alert("💥SR");
    }
}

lot.onclick = randoms;

function average(){
    function score(eng, math, jpn){
        eng = parseInt(eng,10);
        math = parseInt(math,10);
        jpn = parseInt(jpn,10);
    
        let avg = (eng+math+jpn)/ 3 
        window.alert(`平均点は${avg}点です`)
    }
    
    const numE = window.prompt("英語の点数を半角整数で入力");
    const numM = window.prompt("数学の点数を半角整数で入力");
    const numJ = window.prompt("国語の点数を半角整数で入力");
    
    score(numE,numM,numJ);
}

scoreavg.onclick = average;

