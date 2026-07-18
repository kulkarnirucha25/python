import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class BallPanel extends JPanel implements Runnable, MouseListener {

    int x = 50, y = 50;
    int dx = 3, dy = 3;
    Thread t;

    BallPanel() {
        addMouseListener(this);
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLUE);
        g.fillOval(x, y, 40, 40);
    }

    public void run() {
        while (true) {
            x += dx;
            y += dy;

            if (x <= 0 || x >= getWidth() - 40)
                dx = -dx;

            if (y <= 0 || y >= getHeight() - 40)
                dy = -dy;

            repaint();

            try {
                Thread.sleep(20);
            } catch (Exception e) {
            }
        }
    }

    public void mousePressed(MouseEvent e) {
        if (t == null) {
            t = new Thread(this);
            t.start();
        }
    }

    public void mouseClicked(MouseEvent e) {}
    public void mouseReleased(MouseEvent e) {}
    public void mouseEntered(MouseEvent e) {}
    public void mouseExited(MouseEvent e) {}
}

public class BouncingBall {
    public static void main(String[] args) {
        JFrame f = new JFrame("Bouncing Ball");
        BallPanel p = new BallPanel();

        f.add(p);
        f.setSize(500, 400);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}