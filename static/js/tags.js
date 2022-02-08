const origin_tags = document.querySelectorAll("#origin_tags li")
const tagbox = document.querySelector(".tag_box");
const btns = document.querySelectorAll(".tag_box button");

for(let i=0; i<btns.length; i++){
    for(let j=0; j<origin_tags.length; j++){
        if (btns[i].innerHTML === origin_tags[j].innerHTML) {
            btns[i].classList.toggle("selected");
        };
    }
}

function getText() {
    let tags = document.querySelector("#tags");
    let selectedBtns = document.querySelectorAll(".selected");
    tags.value = ''
    selectedBtns.forEach((btn)=>{
        tags.value = tags.value + btn.innerHTML
        // console.log(btn.innerHTML);
    });
    // console.log(tags.value)
};

function toggleBtn(event) {
    event.target.classList.toggle("selected");
    // console.log("clicked");
    getText();
};

btns.forEach((btn) => {
    btn.addEventListener("click", toggleBtn);
});
