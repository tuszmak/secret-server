import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import { userEvent } from "@testing-library/user-event";
import NumberInput from "@/components/NumberInput";


describe("Render", () => {
    it("Should have a label", () => {
      render(<NumberInput />);
      const label = screen.getByTestId("number-label");
      expect(label).toBeInTheDocument();
    });
    it("Should have a span text in the label", () => {
      render(<NumberInput />);
      const span = screen.getByText("How many visits do you allow?");
      expect(span).toBeInTheDocument();
    });
    it("Should have a number input field", () => {
      render(<NumberInput />);
      const input = screen.getByTestId("number-input");
      expect(input).toBeInTheDocument();
    });
    it("Should have a placeholder", () => {
      render(<NumberInput />);
      const input = screen.getByTestId("number-input");
      expect(input).toBeInTheDocument();
  });
  it("Should have an input that is required", ()=>{
      render(<NumberInput />)
      const input = screen.getByTestId("number-input");
      expect(input).toBeRequired()
    })
    it("Should have an input that only accepts positive numbers", ()=>{
      render(<NumberInput />)
      const input : HTMLInputElement = screen.getByTestId("number-input");
      const minAttr = parseInt(input.getAttribute("min") || "")
      expect(minAttr).toBe(1)
    })
  });
  describe("Behavior", () => {
    const mockHandleChange = jest.fn();
    it("Should be able to add date to date", async () => {
      render(<NumberInput handleChange={mockHandleChange} />);
      const input : HTMLInputElement = screen.getByTestId("number-input");
      await userEvent.type(input, "420");
      expect(mockHandleChange).toHaveBeenCalled();
      expect(input.value).toBe("420")
    });
  });
  