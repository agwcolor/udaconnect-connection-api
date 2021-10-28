from datetime import datetime
import time
from concurrent import futures

from app.udaconnect.schemas import (
    ConnectionSchema
)
from app.udaconnect.services import ConnectionService
from flask import request
from flask_accepts import responds
from flask_restx import Namespace, Resource
from typing import Optional, List
import grpc
from . import connection_pb2
from . import connection_pb2_grpc
# TODO: unable to get grpcio-reflection to work
# from grpcio-reflection import reflection

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


# @api.route("/persons/<person_id>/connection")
# @api.param("start_date", "Lower bound of date range", _in="query")
# @api.param("end_date", "Upper bound of date range", _in="query")
# @api.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(connection_pb2_grpc.ConnectionServiceServicer):
    # @responds(schema=ConnectionSchema, many=True)
    # def get(self, request, context) -> ConnectionSchema:
    def get(self, request, context):
        '''
        person_id: request.args.get("person_id", 5)
        start_date: datetime = datetime.strptime(
            request.args["start_date"], DATE_FORMAT
        )
        end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
        distance: Optional[int] = request.args.get("distance", 5)
        
        results = ConnectionService.find_contacts(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            meters=distance,
        )
        '''
        
        results = request.person_id
        print(results, "These are the results returned from gRPC call to ConnectionService")
        return results


# Initialize gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    connection_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionDataResource(), server)

    print("Server starting on port 5005...")

    server.add_insecure_port("[::]:5005")
    server.start()
    # Keep thread alive
    server.wait_for_termination()

serve()