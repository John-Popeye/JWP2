console.log("test")



document.getElementById('save_button').onclick = val => {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://127.0.0.1:5000/save', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
    description: document.getElementById('description').value,
    dueDate: document.getElementById('dueDate').value,
    creator: document.getElementById('creator').value
}))
    window.location.reload(true);
}


function deletePost(id) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://127.0.0.1:5000/delete', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        id: id,
    }))
    window.location.reload(true);
  }