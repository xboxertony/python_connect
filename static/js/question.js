var ws;
document.getElementById("lname").focus()
function myFunction() {
  ws = new WebSocket("ws://localhost:3000/actions");

  ws.onopen = function () {
    //   console.log("ok");
    //   document.getElementById("conn_status").style.display = "flex";
    ws.send(JSON.stringify({"ok":"socket open"}));
  };

  ws.onclose = function (evt) {
    //   document.getElementById("conn_status").style.display = "none";
  };

  ws.onmessage = function (evt) {
    console.log(evt)
    var para = document.createElement("div");
    para.innerHTML = evt.data;
    para.dataset.name = "客服";
    para.dataset.time = get_time()
    para.classList.add("para");
    para.classList.add("chat_box");
    document.getElementById("main_chat").appendChild(para);
    document.getElementById("main_chat").scrollTo(0,document.getElementById("main_chat").scrollHeight-400);
    console.log(document.body.scrollHeight);
  };
}

myFunction();

function get_time(){
  let current_time = new Date()
  return `${current_time.getHours()<10?"0"+current_time.getHours():current_time.getHours()}:${current_time.getMinutes()<10?"0"+current_time.getMinutes():current_time.getMinutes()}:${current_time.getSeconds()<10?"0"+current_time.getSeconds():current_time.getSeconds()}`
}

function sendText(text) {
  var para = document.createElement("div");
  para.innerHTML = text
  para.classList.add("user");
  para.classList.add("chat_box");
  para.dataset.name = "user";
  para.dataset.time = get_time()
  document.getElementById("main_chat").appendChild(para);
  ws.send(JSON.stringify({"ok":text}));
  document.getElementById('lname').innerHTML = ""
}