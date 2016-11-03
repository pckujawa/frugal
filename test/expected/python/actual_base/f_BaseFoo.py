#
# Autogenerated by Frugal Compiler (1.20.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#



from threading import Lock

from frugal.middleware import Method
from frugal.exceptions import FRateLimitException
from frugal.processor import FBaseProcessor
from frugal.processor import FProcessorFunction
from thrift.Thrift import TApplicationException
from thrift.Thrift import TMessageType

from actual_base.python.ttypes import *


class Iface(object):

    def basePing(self, ctx):
        """
        Args:
            ctx: FContext
        """
        pass


class Client(Iface):

    def __init__(self, transport, protocol_factory, middleware=None):
        """
        Create a new Client with a transport and protocol factory.

        Args:
            transport: FSynchronousTransport
            protocol_factory: FProtocolFactory
            middleware: ServiceMiddleware or list of ServiceMiddleware
        """
        if middleware and not isinstance(middleware, list):
            middleware = [middleware]
        self._transport = transport
        self._protocol_factory = protocol_factory
        self._oprot = protocol_factory.get_protocol(transport)
        self._iprot = protocol_factory.get_protocol(transport)
        self._write_lock = Lock()
        self._methods = {
            'basePing': Method(self._basePing, middleware),
        }

    def basePing(self, ctx):
        """
        Args:
            ctx: FContext
        """
        return self._methods['basePing']([ctx])

    def _basePing(self, ctx):
        self._send_basePing(ctx)
        self._recv_basePing(ctx)

    def _send_basePing(self, ctx):
        oprot = self._oprot
        with self._write_lock:
            oprot.get_transport().set_timeout(ctx.get_timeout())
            oprot.write_request_headers(ctx)
            oprot.writeMessageBegin('basePing', TMessageType.CALL, 0)
            args = basePing_args()
            args.write(oprot)
            oprot.writeMessageEnd()
            oprot.get_transport().flush()

    def _recv_basePing(self, ctx):
        self._iprot.read_response_headers(ctx)
        _, mtype, _ = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            if x.type == FRateLimitException.RATE_LIMIT_EXCEEDED:
                raise FRateLimitException(x.message)
            raise x
        result = basePing_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        return

class Processor(FBaseProcessor):

    def __init__(self, handler, middleware=None):
        """
        Create a new Processor.

        Args:
            handler: Iface
        """
        if middleware and not isinstance(middleware, list):
            middleware = [middleware]

        super(Processor, self).__init__()
        self.add_to_processor_map('basePing', _basePing(Method(handler.basePing, middleware), self.get_write_lock()))


class _basePing(FProcessorFunction):

    def __init__(self, handler, lock):
        self._handler = handler
        self._lock = lock

    def process(self, ctx, iprot, oprot):
        args = basePing_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = basePing_result()
        try:
            self._handler([ctx])
        except FRateLimitException as ex:
            with self._lock:
                _write_application_exception(ctx, oprot, FRateLimitException.RATE_LIMIT_EXCEEDED, "basePing", ex.message)
                return
        with self._lock:
            oprot.write_response_headers(ctx)
            oprot.writeMessageBegin('basePing', TMessageType.REPLY, 0)
            result.write(oprot)
            oprot.writeMessageEnd()
            oprot.get_transport().flush()


def _write_application_exception(ctx, oprot, type, method, message):
    x = TApplicationException(type=type, message=message)
    oprot.write_response_headers(ctx)
    oprot.writeMessageBegin(method, TMessageType.EXCEPTION, 0)
    x.write(oprot)
    oprot.writeMessageEnd()
    oprot.get_transport().flush()


class basePing_args(object):
    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('basePing_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class basePing_result(object):
    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('basePing_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
