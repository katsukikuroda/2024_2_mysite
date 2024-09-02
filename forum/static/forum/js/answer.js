function change1(){
    window.alert("Hello");
};

hello.onclick = change1;

function change2(){
    const str = window.prompt("入力してください");
    window.alert(str);
};

shows.onclick = change2;


function levelup (){
    for (let i = 1; i <= 9; i++) {

        window.alert("レベルは" + i + "です。");
      
        // window.alert(`レベルは${i}です。`);
      
      }
};

up.onclick = levelup;

"use strict";
function randoms (){
    const random = Math.floor(Math.random()*10);
    if (random < 6){
        window.alert("N");
    }else if (random < 9){
        window.alert("✨R")
    }else {
        window.alert("💥SR")
    }
};

lot.onclick = randoms;


function average (){
    function score(eng, math, jpn) {
    
        eng = parseInt(eng, 10);
    
        math = parseInt(math, 10);
    
        jpn = parseInt(jpn, 10);
    
        let avg = (eng + math + jpn) / 3;
    
        window.alert("平均点は" + avg + "点です。");
    
    }
    
    const numE = window.prompt("英語の点数を半角整数で入力");
    
    const numM = window.prompt("数学の点数を半角整数で入力");
    
    const numJ = window.prompt("国語の点数を半角整数で入力");
    
    score(numE, numM, numJ);
};

scoreavg.onclick = average;

function q1 (){
    let n = window.prompt("① 半角整数を入力");
    
    let sum = 0;
    
    for (let i = 1; i <= n; i++) {
    
      sum = sum + i;
    
    }
    
    window.alert(`① ${n}回足した時の和は${sum}です。`);
    // window.alert("①" + n + "回足した時の和は" + sum + "です。");
};

add.onclick = q1;

function q2 (){
    let n = window.prompt("② 半角整数を入力");

    sum = 0;
    
    for (let i = 1; i <= n; i++) {
    
      if (i % 2 === 0) {
    
        sum = sum + i;
    
      } else {
    
        sum = sum - i;
    
      }
    
    }
    
    window.alert(`② ${n}回足した時の和は${sum}です。`);
};

addsubstract.onclick = q2;

const select = document.querySelector("select");
const html = document.querySelector("html");
document.body.style.padding = "10px";

function update(bgColor, textColor) {
    html.style.backgroundColor = bgColor;
    html.style.color = textColor;
  }
  

const theme = document.getElementById("theme");
theme.onchange = function (){
    if(theme.value === "black"){
        update("black", "white");
    }else{
        update("white", "black");
    }
};
