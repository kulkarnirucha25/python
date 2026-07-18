import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Calculator extends JFrame implements ActionListener {
    private JTextField display;
    private double num1 = 0, num2 = 0, result = 0;
    private char operator;

    // Button labels arranged in a logical grid layout
    private final String[] buttons = {
        "7", "8", "9", "/", "sqrt",
        "4", "5", "6", "*", "sqr",
        "1", "2", "3", "-", "cube",
        "C", "0", "=", "+", "%"
    };

    public Calculator() {
        // Frame Settings
        setTitle("Standard Calculator");
        setSize(400, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        // Display Screen
        display = new JTextField();
        display.setFont(new Font("Arial", Font.BOLD, 28));
        display.setEditable(false);
        display.setHorizontalAlignment(JTextField.RIGHT);
        display.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        add(display, BorderLayout.NORTH);

        // Buttons Panel
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(4, 5, 8, 8));
        panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        for (String str : buttons) {
            JButton button = new JButton(str);
            button.setFont(new Font("Arial", Font.BOLD, 16));
            button.addActionListener(this);
            panel.add(button);
        }

        add(panel, BorderLayout.CENTER);
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();

        // Handle Clear
        if (command.equals("C")) {
            display.setText("");
            num1 = num2 = result = 0;
            return;
        }

        // Handle Digits
        if ((command.charAt(0) >= '0' && command.charAt(0) <= '9')) {
            display.setText(display.getText() + command);
            return;
        }

        // Handle Instant Single-Operand Operations
        if (command.equals("sqrt") || command.equals("sqr") || command.equals("cube")) {
            if (!display.getText().isEmpty()) {
                double val = Double.parseDouble(display.getText());
                if (command.equals("sqrt")) result = Math.sqrt(val);
                else if (command.equals("sqr")) result = val * val;
                else if (command.equals("cube")) result = val * val * val;
                
                display.setText(String.valueOf(result));
            }
            return;
        }

        // Handle Multi-Operand Binary Operators (+, -, *, /, %)
        if (command.equals("+") || command.equals("-") || command.equals("*") || command.equals("/") || command.equals("%")) {
            if (!display.getText().isEmpty()) {
                num1 = Double.parseDouble(display.getText());
                operator = command.charAt(0);
                display.setText("");
            }
            return;
        }

        // Handle Evaluation
        if (command.equals("=")) {
            if (!display.getText().isEmpty() && operator != '\0') {
                num2 = Double.parseDouble(display.getText());
                switch (operator) {
                    case '+': result = num1 + num2; break;
                    case '-': result = num1 - num2; break;
                    case '*': result = num1 * num2; break;
                    case '/': 
                        if (num2 == 0) {
                            display.setText("Error (Div by 0)");
                            return;
                        }
                        result = num1 / num2; 
                        break;
                    case '%': result = num1 % num2; break;
                }
                display.setText(String.valueOf(result));
                operator = '\0'; // Reset operator
            }
        }
    }
    public static void main(String[] args) {
        // Run GUI inside the Event Dispatch Thread (EDT) for thread-safety
        SwingUtilities.invokeLater(Calculator::new);
    }
}