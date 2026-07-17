OSI MODEL
Open systems interconnect(OSI) model is a framework that standardizes the functions of telecommunicaton or computing system into 7 distinct abstract layers.  The whole purpose of the OSI model is to break down complex network communication in smaller concept to make sure system can communicate seamlessly. Like the name suggest, OSI show the whole complexity of how different system communicate but broken in simpler concepts OR layers. 
The OSI model is broken down into 7 layers. 
Layer 1 - Physical(please) 
Layer 2 - data(do ) 
Layer 3 - network (not) 
Layer 4 - transport (throw) 
Layer 5 - session (sausage) 
Layer 6 - presentation(pizza) 
Layer 7 - application (away) 
The Mnemonic for the OSI model in ascending order(layer 1- 7) is Please Do Not Throw Sausage Pizza Away. 
When inverted(layer 7 - 1), its slogan becomes All People Seem To Need Data Processing. 
In OSI model, data is classified as Protocol Data Unit(PDU). At the bottom 4 layers, the PDU is refered to by many names. They are;
layer 1 - Bits 
Layer 2 - Frames 
Layer 3 - Packet 
Layer 4 - Segments 

Why the OSI model? 
It's a way to categorize anything happening within our network. This makes communication and troubleshooting easier 

Layer 1 - physical layer. 
This level is concerned with how bits(data) is gotten or moved across the network. (the representation or conversion of data as 0s and 1s or  electrical signal to be able to flow throught cables and hardwares at this layer.) 
Example of layer 1 components: Ethernet cable, fiber optic cable, network adapter or card etc 
Alternate mark inversion 
At layer 1, not only does bit and its component live here but some etiquette in relation to those components too. Example is the wiring standard. Eg. T568B standard. 
This layer also entails the physical topology of the network. Eg: bus topology, star topology, ring topology etc. 
At the physical layer, synchronization takes place. This is simply the agreement between the sender and receiver about when bits begins and stops. This can be done through asynchronous communication or synchronization and synchronous synchronization. 
Bandwith usage too takes place at this layer. 
Multiplexing: how different conversation is sent at the same time on the same media 

Layer 2 - data link 
This layer is broken down into 2 different layers. 
1.  Media Access Control - Physical addressing of a network device happens at this layer. The Mac address is a 48 bit address that give a network device it's uniqueness or from every other device on the network or internet. 

*Logical topology 
*Method of data transmission 

2. Logical Link control 
*connection services 
*Error notification services 
*Synchronization of transmission 

Types of synchronization
Isochronous synchronization: Devices look to connect to a common external device for clocking
Asynchronous synchronization: Device use their internal clock and also use start or stop bits.
Synchronous synchronization: Clocking is shared between sender and receiver over a separate channel. Example of layer 2 device is Ethernet switch 

Layer 3 - Network 
*Logical Addressing (IP)
switching(packet switching ) 
*connection services (flow control) 

Layer 4 - Transport
Transmission Control Protocol(TCP): TCP is termed as one of the reliable protocols. For computer to be able to communicate or send segments over TCP, the TCP 3- way handshake is required. They are:
Synchronization(syn)
Synchronization and acknowledgement (SYN-ACK)
Acknowledgement (ACK) 
Eg: so there are 2 computers on a network namely: computer on and computer 2. If computer one wants to communicate or send segments via TCP to computer 2, computer 1 be like "hey, computer 2, I want to communicate with you" (syn). Then computer 2 be like "oh computer one wants to communicate with me, I'm cool (ack) and then tell computer Im okay we can communicate (syn). This forms the SYN-ACK. Then computer 1 also acknowledges computer 2's readiness to communicate(ACK). This for the TCP 3 - way handshake (SYN > SYN- ACK > ACK).

User datagram protocol(UDP) UDP is termed as an unreliable protocol. Tho unreliable, it's is one of the best protocol for voice and video transmission. Real-time transfer protocol: RTP  is a protocol use to transfer voice and video over a network. The RTP is classified under UDP, a layer 4 protocol
Windowing
Buffering Applications make request and service receive those request.. These request are identified through port addresses 

Layer 5 - session layer Responsible for
Establishing a session
Maintaining a session
Tearing down a session 

Layer 6 - presentation layer -Data formatting -Encryption 

Layer 7 - Application -Application service -Service advertisement
