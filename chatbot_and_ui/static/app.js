class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }
        this.state = false;
        this.messages = [];
    }

    display() {
        // Extract argunment
        const {openButton, chatBox, sendButton} = this.args;
        // listen to events, open or send
        openButton.addEventListener('click', () => this.toggleState(chatBox))
        sendButton.addEventListener('click', () => this.onSendButton(chatBox))
        // listen to enter
        const node = chatBox.querySelector('input');
        node.addEventListener('keyup', ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // this is used to display or hide the window
        if (this.state) {
            chatbox.classList.add('chatbox--active')
        }
        else {
            chatbox.classList.remove('chatbox--active')
        }
    }
    
    onSendButton(chatbox) {
        // get text from user input
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        // check if it is empty
        if (text1 === "") {
            return;
        }

        let msg1 = {name: "User", message: text1}
        this.messages.push(msg1);

        // "PATH/predict"
        fetch($SCRIPT_ROOT + '/predict', {
            method: 'POST', 
            body: JSON.stringify({message: text1}), 
            mode: 'cors',
            headers: {'Content-Type': 'application/json'}
        })
        // after sending post request  get the json back
        .then(r => r.json())
        // send the message back to the user
        .then(r => {
            let msg2 = {name: "Sam", message: r.answer};
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''
        // else it is an error
        }).catch((error) => {
            console.error('Error: ', error);
            this.updateChatText(chatbox)
            textField.value = ''
        });
    }

    updateChatText(chatbox) {
        var html = '';
        // go over the messages and modify if it is the user or the chatbot in the html
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Sam") {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
        });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}

const chatbox = new Chatbox();
chatbox.display();


// class Chatbox {
//     constructor() {
//         this.args = {
//             openButton: document.querySelector('.chatbox__button'),
//             chatBox: document.querySelector('.chatbox__support'),
//             sendButton: document.querySelector('.send__button')
//         }

//         this.state = false;
//         this.messages = [];
//     }

//     display() {
//         const {openButton, chatBox, sendButton} = this.args;

//         openButton.addEventListener('click', () => this.toggleState(chatBox))

//         sendButton.addEventListener('click', () => this.onSendButton(chatBox))

//         const node = chatBox.querySelector('input');
//         node.addEventListener("keyup", ({key}) => {
//             if (key === "Enter") {
//                 this.onSendButton(chatBox)
//             }
//         })
//     }

//     toggleState(chatbox) {
//         this.state = !this.state;

//         // show or hides the box
//         if(this.state) {
//             chatbox.classList.add('chatbox--active')
//         } else {
//             chatbox.classList.remove('chatbox--active')
//         }
//     }

//     onSendButton(chatbox) {
//         var textField = chatbox.querySelector('input');
//         let text1 = textField.value
//         if (text1 === "") {
//             return;
//         }

//         let msg1 = { name: "User", message: text1 }
//         this.messages.push(msg1);

//         fetch($SCRIPT_ROOT + '/predict', {
//             method: 'POST',
//             body: JSON.stringify({ message: text1 }),
//             mode: 'cors',
//             headers: {
//               'Content-Type': 'application/json'
//             },
//           })
//           .then(r => r.json())
//           .then(r => {
//             let msg2 = { name: "Sam", message: r.answer };
//             this.messages.push(msg2);
//             this.updateChatText(chatbox)
//             textField.value = ''

//         }).catch((error) => {
//             console.error('Error:', error);
//             this.updateChatText(chatbox)
//             textField.value = ''
//           });
//     }

//     updateChatText(chatbox) {
//         var html = '';
//         this.messages.slice().reverse().forEach(function(item, index) {
//             if (item.name === "Sam")
//             {
//                 html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
//             }
//             else
//             {
//                 html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
//             }
//           });

//         const chatmessage = chatbox.querySelector('.chatbox__messages');
//         chatmessage.innerHTML = html;
//     }
// }


// const chatbox = new Chatbox();
// chatbox.display();