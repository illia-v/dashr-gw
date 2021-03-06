import React from "react";
import { Redirect } from "react-router";
import DjangoCSRFToken from 'django-react-csrftoken';
import Button from 'react-bootstrap/lib/Button';
import Panel from 'react-bootstrap/lib/Panel';
import Form from 'react-bootstrap/lib/Form';
import FormGroup from 'react-bootstrap/lib/FormGroup';
import FormControl from 'react-bootstrap/lib/FormControl';
import ControlLabel from 'react-bootstrap/lib/ControlLabel';
import HelpBlock from 'react-bootstrap/lib/HelpBlock';
import Col from 'react-bootstrap/lib/Col';
import { LinkContainer } from 'react-router-bootstrap';

import Transaction from './Transaction';

export default class Deposit extends Transaction {
    constructor(props) {
        super(props);
        this.transactionType = 'deposit';
    }

    render() {
        if (this.state && this.state.statusUrl) {
            return <Redirect to={this.state.statusUrl} />;
        }
        return (
            <Panel className="panel-wrapper panel-wrapper-container">
                <Panel.Heading>Deposit DASH to Ripple</Panel.Heading>
                <Panel.Body>
                    <Col sm={12} md={6}>
                        <Form onSubmit={this.handleFormSubmit.bind(this)} id="transaction-form">
                            <DjangoCSRFToken/>
                            <FormGroup controlId="ripple_address_input"
                                       validationState={this.getFieldValidationState('ripple_address')}>
                                <ControlLabel>Your Ripple Address:</ControlLabel>
                                <FormControl type="text" name="ripple_address" required />
                                {this.getFieldError('ripple_address')}
                                <FormControl.Feedback />
                            </FormGroup>
                            <FormGroup controlId="dash_to_transfer_input"
                                       validationState={this.getFieldValidationState('dash_to_transfer')}>
                                <ControlLabel>
                                    Deposit Amount (Min. {this.state.minAmount} DASH):
                                </ControlLabel>
                                <FormControl type="number"
                                             name="dash_to_transfer"
                                             onInput={this.changeReceiveAmountField.bind(this)}
                                             step="0.00000001"
                                             min={this.state.minAmount}
                                             required/>
                                {this.getFieldError('dash_to_transfer')}
                                <FormControl.Feedback />
                            </FormGroup>
                            <FormGroup id="receive-amount-form-group">
                                <ControlLabel>Receive Amount:</ControlLabel>
                                <FormControl id="dash_to_receive_input" disabled/>
                            </FormGroup>
                            <Button block type="submit">Start</Button>
                            <HelpBlock>
                                <LinkContainer to="/deposit/how-to/">
                                    <Button bsStyle="link">Need help?</Button>
                                </LinkContainer>
                            </HelpBlock>
                        </Form>
                    </Col>
                </Panel.Body>
            </Panel>
        );
    }
}
