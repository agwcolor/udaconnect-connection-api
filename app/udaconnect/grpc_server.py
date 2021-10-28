
import grpc
import logging
from concurrent import futures
from . import connection_pb2
from . import connection_pb2_grpc
from controllers import ConnectionDataResource


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    connection_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionDataResource(), server)
    logging.log(logging.INFO, 'gRPC server starting on port 5000.')
    server.add_insecure_port("[::]:5005")
    server.start()
    server.wait_for_termination()
    
if __name__ == '__main__':
    serve()