kafka:
create an empty python project
add docker-compose.yaml as configuration:
{
				version: '3.8'

		services:
		  kafka:
			image: confluentinc/cp-kafka:7.7.8
			container_name: kafka
			ports:
			  - "9092:9092"
			#   - "29092:29092"
			environment:
			  KAFKA_node_ID: 1
			  kafka_kraft_mode: "true"
			  cluster_id: "sdlaksjafads_dasas-asdasd"
			  kafka_process_roles: "broker,controller"
			  kafka_controller_quorum_voters: "1@kafka:9093"
			  kafka_offsets_topic_replication_factor: 1 #metadata topic replication factor, here no backup
			  kafak_listeners: PLAINTEXT://kafka:9092,CONTROLLER://kafka:9093
			  kafka_advertised_listeners: PLAINTEXT://localhost:9092
			  kafka_connection_listener_name: controller
			  kafak_log_dirs: /tmp/kraft-combined-logs
			volumes:
			  - kafka_kraft:/var/lib/kafka/data  

		volumes:
		  kafka_kraft
}
Install docker -> run it
pull kafka image 7.7.3: https://hub.docker.com/layers/confluentinc/cp-kafka/7.7.8/images/sha256-0ee551e2e948c5dcd12366216046250584bcc2ddba1171dc7246c5ff7589fa82
run kafka with docker-compose up
to be able to communicate kafka install an extension
confluent_kafka:  pip3 install confluent-kafka
list all the topics
docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --list

neelam6998194
n331@mIbkr

for equate plus
ibkr detsils:
         
     SAP ISIN: DE0007164600
     
     account number:  U24927361 
     email: fop-transfer-in@interactivebrokers.com     
     clearing: REAG/DEAG TMBECH22THE BUYR/SELL TMBECH22THE DAKV8587000 PSET/DAKVDEFFXXX
     brokerage code: 
     broker:Interactive Brokers Australia Pty Ltd
     swift or bic: IBKRUS33XXX.. WILL BE PICKED UP BY ITS OWN
address:Level 11, 175 Pitt Street, Sydney NSW 2000, Australia   

  
  winston hills mall: 0298387822.. saturday they have available 
  +61296869222: Myhealth Baulkham Hills Medical Centre : 10.15 am 
  
  2-5: rouse hill caliing center 

On my cv: add m

2 rounds of interview : 
    
    star response: situation, 
    car: contact ectional result.
    
    
    CommSec details
    client id: 43036305 pin 1105
    58126203
    
    
    account number: U25901031
    email: 
        brokerage coge: 0534
        swift or bic code: 
            
            
equateplus login : 6998194
pswd: n331@mEquate
website: 
    
    
    slalom password: r4rXWF!x43!CBb4
    
    
Here are the details I need to transfer the shares: 
Name of Broker/Custodian: FLatexdegiro se
Broker/Custodian Account Number: 1032276791
Name on Account: Neelam kumari
Country of Broker/Custodian: Germany
Contact email for Broker/Custodian: N/A mbx-participant-services@equatex.com
Account type (tick only one box): Individual
Asset details: 
    Company name: SAP
 Trading Exchange:  xetra
 Symbol/ISIN/CUSIP: de0007164600