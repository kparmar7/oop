from abc import ABC, abstractmethod

class OutboundEvent(ABC):

    def construct_and_send_event(self):
        print('parent construct_and_send_event')
        return self._send_event()

    def get_shipment_construct_and_send(self):
        print('parent get_shipment_construct_and_send')
        self.construct_and_send_event()
    
    def do_send(self):
        print('parent do_send')

    @abstractmethod
    def _send_event(self):
        ## returns do_send with modified event
        print('parent _send_event')
        raise NotImplementedError

class OutboundTripLegEvent(OutboundEvent):
    def contruct_and_send(self):
        print('child contruct_and_send')
        super().get_shipment_construct_and_send()

    
    def _send_event(self):
        print('child _send_event')
        return super().do_send()
    
outbound_event = OutboundTripLegEvent()
outbound_event.contruct_and_send()
