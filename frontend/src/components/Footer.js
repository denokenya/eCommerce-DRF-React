import React from "react";
import { Container, Row, Col } from "react-bootstrap";

export default function Footer() {
  return (
    <footer>
      <hr/>
      <Container>
        <Row>
          <Col className="text-center py-3">Copyright &copy; eCommerce</Col>
        </Row>
      </Container>
    </footer>
  );
}
