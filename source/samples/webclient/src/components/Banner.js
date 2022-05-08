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
import { Auth } from 'aws-amplify';
import logo from '../logo.png';

declare var awsConfig;

class Banner extends React.Component {
    constructor(props) {
        super(props);
	this.signOut = this.signOut.bind(this);
    }
	
    signOut = () => {
        Auth.signOut()
	.then(data => console.log(data))
	.catch(err => console.log(err));
	window.location.reload(true);
    }

    render() {
        return (
            <div className='banner'>
		<button className='banner--language'>{awsConfig.language}</button>
		<span className='banner--logo'><img src={logo} alt={'logo'}/></span>
		<button onClick={this.signOut} className="signOutButton">Sign Out</button>
            </div>
        )
    }
}

export default Banner;
