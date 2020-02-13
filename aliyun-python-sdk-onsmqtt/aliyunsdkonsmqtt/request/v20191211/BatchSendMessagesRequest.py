# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class BatchSendMessagesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OnsMqtt', '2019-12-11', 'BatchSendMessages','onsmqtt')
		self.set_method('POST')

	def get_NoPersistFlag(self):
		return self.get_query_params().get('NoPersistFlag')

	def set_NoPersistFlag(self,NoPersistFlag):
		self.add_query_param('NoPersistFlag',NoPersistFlag)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Messagess(self):
		return self.get_query_params().get('Messagess')

	def set_Messagess(self,Messagess):
		for i in range(len(Messagess)):	
			if Messagess[i].get('Payload') is not None:
				self.add_query_param('Messages.' + str(i + 1) + '.Payload' , Messagess[i].get('Payload'))
			for j in range(len(Messagess[i].get('Topicss'))):
				if Messagess[i].get('Topicss')[j] is not None:
					self.add_query_param('Messages.' + str(i + 1) + '.Topics.'+str(j + 1), Messagess[i].get('Topicss')[j])
			if Messagess[i].get('Id') is not None:
				self.add_query_param('Messages.' + str(i + 1) + '.Id' , Messagess[i].get('Id'))
			if Messagess[i].get('ReceiptId') is not None:
				self.add_query_param('Messages.' + str(i + 1) + '.ReceiptId' , Messagess[i].get('ReceiptId'))
