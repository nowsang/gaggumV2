package com.gaggum.plantservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@EnableDiscoveryClient
@SpringBootApplication
public class PlantserviceApplication {

	public static void main(String[] args) {
		SpringApplication.run(PlantserviceApplication.class, args);
	}

}
