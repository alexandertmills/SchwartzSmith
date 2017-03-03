// CCCEntryPoint.java

import py4j.GatewayServer;
import no.hials.crosscom.CrossComClient;

import java.io.IOException;
import java.util.Scanner;


public class ClientEntryPoint {

    private CrossComClient client;

	public ClientEntryPoint(String address, int port) {
        System.out.println("Attempting to connect to KUKAVARPROXY...");
        try {
            client = new CrossComClient(address, port);
            System.out.format("Started client on %s:%d\n", address, port);
        } catch (IOException ex) {
            System.out.println(ex);
            System.out.println("Terminating...");
            System.exit(1);
        }
	}

    public CrossComClient getClient() {
        return client;
    }

    public static void main(String[] args) {

        String address = "192.168.1.12";
        int port = 7000;

        GatewayServer gatewayServer = new GatewayServer(new ClientEntryPoint(address, port));
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }

}