package com.gaggum.robotservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@EnableDiscoveryClient
@SpringBootApplication
public class RobotserviceApplication {

	public static void main(String[] args) {
		SpringApplication.run(RobotserviceApplication.class, args);
	}

}
