import Save from "@/pages/save";
import { getByRole, getByTestId, render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import { userEvent } from "@testing-library/user-event";
import Home from "@/pages";
import { describe } from "node:test";
describe("State when there's no link", () => {
  describe("Render", () => {
    it("Should render the back button", () => {
      render(<Save />);
      const backButton = screen.getByText("Back");
      expect(backButton).toBeInTheDocument();
    });
    it("Should render the input fields", () => {
      render(<Save />);
      const secretInput = screen.getByText("What is your secret?");
      const visitInput = screen.getByText("How many visits do you allow?");
      const dateInput = screen.getByText("When should it expire naturally?");
      expect(secretInput).toBeInTheDocument();
      expect(visitInput).toBeInTheDocument();
      expect(dateInput).toBeInTheDocument();
    });
    it("Should render the submit button", () => {
      render(<Save />);
      const submitButton = screen.getByText("Submit");
      expect(submitButton).toBeInTheDocument();
    });
  });
  describe("Behavior", () => {});
  it("Should call handleSubmit when the Submit button is clicked", async () => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve({ test: 100 }),
      })
    ) as jest.Mock;

    render(<Save />);
    const submitButton = screen.getByTestId("submitButton");
    await userEvent.click(submitButton);
    expect(global.fetch).toHaveBeenCalled();
  });
});
