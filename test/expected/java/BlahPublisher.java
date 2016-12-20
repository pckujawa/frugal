/**
 * Autogenerated by Frugal Compiler (1.24.1)
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *
 * @generated
 */

package foo;

import com.workiva.frugal.middleware.InvocationHandler;
import com.workiva.frugal.middleware.ServiceMiddleware;
import com.workiva.frugal.protocol.*;
import com.workiva.frugal.provider.FScopeProvider;
import com.workiva.frugal.transport.FScopeTransport;
import com.workiva.frugal.transport.FSubscription;
import org.apache.thrift.TException;
import org.apache.thrift.TApplicationException;
import org.apache.thrift.transport.TTransportException;
import org.apache.thrift.protocol.*;

import javax.annotation.Generated;
import java.util.logging.Logger;




@Generated(value = "Autogenerated by Frugal Compiler (1.24.1)", date = "2015-11-24")
public class BlahPublisher {

	private static final String DELIMITER = ".";

	private final InternalBlahPublisher target;
	private final InternalBlahPublisher proxy;

	public BlahPublisher(FScopeProvider provider, ServiceMiddleware... middleware) {
		target = new InternalBlahPublisher(provider);
		proxy = (InternalBlahPublisher) InvocationHandler.composeMiddlewareClass(target, InternalBlahPublisher.class, middleware);
	}

	public void open() throws TException {
		target.open();
	}

	public void close() throws TException {
		target.close();
	}

	public void publishDoStuff(FContext ctx, Thing req) throws TException {
		proxy.publishDoStuff(ctx, req);
	}

	protected static class InternalBlahPublisher {

		private FScopeProvider provider;
		private FScopeTransport transport;
		private FProtocol protocol;

		protected InternalBlahPublisher() {
		}

		public InternalBlahPublisher(FScopeProvider provider) {
			this.provider = provider;
		}

		public void open() throws TException {
			FScopeProvider.Client client = provider.build();
			transport = client.getTransport();
			protocol = client.getProtocol();
			transport.open();
		}

		public void close() throws TException {
			transport.close();
		}

		public void publishDoStuff(FContext ctx, Thing req) throws TException {
			String op = "DoStuff";
			String prefix = "";
			String topic = String.format("%sBlah%s%s", prefix, DELIMITER, op);
			transport.lockTopic(topic);
			try {
				protocol.writeRequestHeader(ctx);
				protocol.writeMessageBegin(new TMessage(op, TMessageType.CALL, 0));
				req.write(protocol);
				protocol.writeMessageEnd();
				transport.flush();
			} finally {
				transport.unlockTopic();
			}
		}
	}
}
