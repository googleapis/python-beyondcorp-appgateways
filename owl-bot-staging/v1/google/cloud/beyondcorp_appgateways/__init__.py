# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.cloud.beyondcorp_appgateways_v1.services.app_gateways_service.client import AppGatewaysServiceClient
from google.cloud.beyondcorp_appgateways_v1.services.app_gateways_service.async_client import AppGatewaysServiceAsyncClient

from google.cloud.beyondcorp_appgateways_v1.types.app_gateways_service import AppGateway
from google.cloud.beyondcorp_appgateways_v1.types.app_gateways_service import AppGatewayOperationMetadata
from google.cloud.beyondcorp_appgateways_v1.types.app_gateways_service import CreateAppGatewayRequest
from google.cloud.beyondcorp_appgateways_v1.types.app_gateways_service import DeleteAppGatewayRequest
from google.cloud.beyondcorp_appgateways_v1.types.app_gateways_service import GetAppGatewayRequest
from google.cloud.beyondcorp_appgateways_v1.types.app_gateways_service import ListAppGatewaysRequest
from google.cloud.beyondcorp_appgateways_v1.types.app_gateways_service import ListAppGatewaysResponse

__all__ = ('AppGatewaysServiceClient',
    'AppGatewaysServiceAsyncClient',
    'AppGateway',
    'AppGatewayOperationMetadata',
    'CreateAppGatewayRequest',
    'DeleteAppGatewayRequest',
    'GetAppGatewayRequest',
    'ListAppGatewaysRequest',
    'ListAppGatewaysResponse',
)
