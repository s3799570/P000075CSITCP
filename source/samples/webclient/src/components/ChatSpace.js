 /*********************************************************************************************************************
 *  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 *  Licensed under the Apache License Version 2.0 (the 'License'). You may not use this file except in compliance
 *  with the License. A copy of the License is located at
 *
 *      http://www.apache.org/licenses/
 *
 *  or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES
 *  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions
 *  and limitations under the License.
 *********************************************************************************************************************/

/**
 * @author Solution Builders
 */

import React from 'react';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { API, Auth } from 'aws-amplify';
import TextareaAutosize from 'react-textarea-autosize';
import { extractResponse, constructRequest, scrollToBottom, textToSpeech } from '../utils/utilityFunctions';
import mic from '../mic_c.png';
declare var awsConfig;


class ChatSpace extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            messages: [],
            lastResponse: {},
        };
        this.input = React.createRef();
        this.myFunction = this.myFunction.bind(this);
        this.myVoiceFunction = this.myVoiceFunction.bind(this);
        this.myGreetingFunction = this.myGreetingFunction.bind(this);
    }

    // function to process user's input
    async myFunction (event) {
        event.preventDefault();
        if(this.input.current.value) {
            let newState = {messages: [...this.state.messages, {request: this.input.current.value, response: '...'}]}
            let index=this.state.messages.length;
            let requestData = constructRequest(this.state.lastResponse, this.input.current.value);
            this.setState(newState);
            this.input.current.value = '';
            // call API asyncronously
            let params = {
                headers: { Authorization: `Bearer ${(await Auth.currentSession()).getIdToken().getJwtToken()}` },
                body: requestData
            }
            const botName = awsConfig.API.endpoints[0].name;
            const response = await API.post(botName, 'core/', params);
            let currentState = this.state;
            currentState.messages[index].response = response ? extractResponse(response) : "Error!";
            await textToSpeech(currentState.messages[index].response);
            currentState.lastResponse = response ? response : {};
            this.setState(currentState);
        }
    }
 
    // function to process user's input
    async myGreetingFunction() {
        let greetingIntent = 'help'; // THIS IS THE MESSAGE THAT IS SENT TO LEX TO INVOKE GREETING
        let newState = {messages: [...this.state.messages, {request: greetingIntent, response: '...'}]}
        let index=this.state.messages.length;
        let requestData = constructRequest(this.state.lastResponse, greetingIntent);
        this.setState(newState);
        this.input.current.value = '';
        // call API asyncronously
        let params = {
            headers: { Authorization: `Bearer ${(await Auth.currentSession()).getIdToken().getJwtToken()}` },
            body: requestData
        }
        const botName = awsConfig.API.endpoints[0].name;
        const response = await API.post(botName, 'core/', params);
        let currentState = this.state;
        currentState.messages[index].response = response ? extractResponse(response) : "Error!";
        await textToSpeech(currentState.messages[index].response);
        currentState.lastResponse = response ? response : {};
        this.setState(currentState);
     }
 
    myVoiceFunction() {
        if (!window.webkitSpeechRecognition) {
            toast.info("Your browser doesn't support voice to speech API",
              {
                position: "top-center",
                autoClose: false,
                hideProgressBar: false,
                closeOnClick: true,
                pauseOnHover: true,
                draggable: true,
                progress: undefined,
              }
            );
          } else {
            var recognition = new window.webkitSpeechRecognition();
            recognition.lang = awsConfig.language;
            recognition.continuous = true;
            recognition.interimResults = false;
            recognition.start();
            recognition.onresult = function(event) {
              let final_transcript = '';
              for (let i = event.resultIndex; i < event.results.length; ++i) {
                if (event.results[i].isFinal) {
                  final_transcript += event.results[i][0].transcript;
                  recognition.stop();
                }
              }
              document.getElementById('message').value = final_transcript;
              document.getElementById('chat-send').click();
            };
          }
    }

    // function to put request and response html elements on the page
    showConversation(messages) {
        let items = [];
        for (let item=0; item < messages.length; item++) {
            let {request, response} = messages[item];
            items.push(<div className="chat-space--message" key={item.toString() + 'request'}>{request}</div>);
            items.push(<div className="chat-space--response" key={item.toString() + 'response'}>{response}</div>);
        }
        return items;
    }

    // after user input scroll to the bottom so that user can see the response
    componentDidUpdate() {
        scrollToBottom();
    }

    componentDidMount() {
        this.myGreetingFunction();
    }

    render () {     
        let {messages} = this.state;
        return (
            <div className="chat-container">
                <div className="chat-space">
                    {this.showConversation(messages)}
                </div>
                <form className="textbox" id="chat-form" onSubmit={this.myFunction}>
                    <span className='banner--mic-container' onClick={this.myVoiceFunction}> <img className='banner--mic-image' src={mic} alt={'mic'}/></span>
                    <TextareaAutosize maxRows={6} id='message' className="textbox--input" type='text' placeholder='Type a message...' ref={this.input}/>
                    <input type='submit' className="textbox--send" id="chat-send" value='Send'/>
                    <ToastContainer />
                </form>
            </div>
        )
    }
}

export default ChatSpace;
