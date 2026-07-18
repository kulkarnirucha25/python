import javax.swing.*;
import java.awt.event.*;

public class Stopwatch extends JFrame implements Runnable {

    JLabel label;
    JButton start, stop, reset;

    int seconds = 0;
    boolean running = false;
    Thread t;

    Stopwatch() {
        label = new JLabel("0", JLabel.CENTER);

        start = new JButton("Start");
        stop = new JButton("Stop");
        reset = new JButton("Reset");

        add(label, "North");

        JPanel p = new JPanel();
        p.add(start);
        p.add(stop);
        p.add(reset);

        add(p, "South");

        start.addActionListener(e -> {
            if (!running) {
                running = true;
                t = new Thread(this);
                t.start();
            }
        });

        stop.addActionListener(e -> running = false);

        reset.addActionListener(e -> {
            running = false;
            seconds = 0;
            label.setText("0");
        });

        setSize(300, 150);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public void run() {
        while (running) {
            seconds++;
            label.setText("" + seconds);

            try {
                Thread.sleep(1000);
            } catch (Exception e) {
            }
        }
    }

    public static void main(String[] args) {
        new Stopwatch();
    }
}