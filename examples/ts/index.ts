import * as datarobot from "@pulumi/datarobot";

console.log("Creating a DataRobot use case...");

// Create a DataRobot use case
const useCase = new datarobot.UseCase("exampleFromTypescript", {
    name: "An example from TypeScript",
    description: "Description for the example use case",
});

// Export the ID of the example use case
export const exampleId = useCase.id;