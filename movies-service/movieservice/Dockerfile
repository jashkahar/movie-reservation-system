FROM openjdk:17-jdk-slim
WORKDIR /app
COPY target/movieservice-0.0.1-SNAPSHOT.jar movies-service.jar
ENTRYPOINT ["java", "-jar", "movies-service.jar"]
