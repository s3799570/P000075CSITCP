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

var awsConfig = {
    Auth: {

        // OPTIONAL - Amazon Cognito User Pool ID
        // userPoolId: 'us-east-2_iPt7EDs4O',
        userPoolId: "ap-southeast-2_OQKacayCn",

        // OPTIONAL - Amazon Cognito Web Client ID (26-char alphanumeric string)
        // userPoolWebClientId: '2f52skhif0qno07lvlfqu97fr4',
        userPoolWebClientId: "tb7obqd69ahiovql4ccn6oo5e",

        // OPTIONAL - Enforce user authentication prior to accessing AWS resources or not
        mandatorySignIn: false,

        // REQUIRED - Amazon Cognito Region
        region: "ap-southeast-2",
    },
    API: {
      endpoints: [
        {
            name: "Joe",
            endpoint: "https://ycqx2nkpkk.execute-api.ap-southeast-2.amazonaws.com/prod/"

        }
      ]
    },
    language: "en_US",
    botVoice: "Joey",
    cognitoIdentityPool: "ap-southeast-2:c8c2a79d-ee46-404e-bb03-e0a5df41fa5b",
    clientMetadata: { customUserAgent: "AwsSolution/SOL0027/1.6.0" },
};
