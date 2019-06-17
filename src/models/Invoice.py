from src.database import Database

class Invoice(object):
    def __init__(self):
        self.collection = "default"

    def save_to_mongo(self):
        print(self.json())
        result = Database.insert(collection= self.collection, data=self.json())
        if result is None:
            print ("Insertion into database is not successful!")

        else:
            print ("Insertion into database is successful!")

class QInvoice(Invoice):
    def __init__(self, auction_no, obligor_name, seller_no, currency, advanced_amount, gross_gain, platform_fee,
                 net_total_to_be_received, gross_return, net_return, advanced_date, due_date,
                 expected_duration, insured_invoice,obligor_notification, status = "Traded", late_day = 0,
                 rationale = "Within mandate"):
        super().__init__()
        self.auction_no = auction_no
        self.obligor_name = obligor_name
        self.sell_no = seller_no
        self.currency = currency
        self.advanced_amount = advanced_amount
        self.gross_gain = gross_gain
        self.platform_fee = platform_fee
        self.net_total_to_be_received = net_total_to_be_received
        self.gross_return = gross_return
        self.net_return = net_return
        self.advanced_date = advanced_date
        self.due_date = due_date
        self.remitted_date = "NA"
        self.expected_duration = expected_duration
        self.status = status
        self.insured_invoice = insured_invoice
        self.obligor_notification = obligor_notification
        self.rationale = rationale
        self.late_day = late_day
        self.collection = "qupital_invoice"

    def json(self):
        return {
            'id': self.auction_no,
            'auction_no' : self.auction_no,
            'obligor_name' : self.obligor_name,
            'sell_no' : self.sell_no,
            'currency' : self.currency,
            'advanced_amount' : self.advanced_amount,
            'gross_gain' : self.gross_gain,
            'platform_fee' : self.platform_fee,
            'net_total_to_be_received' : self.net_total_to_be_received,
            'gross_return' : self.gross_return,
            'net_return' : self.net_return,
            'advanced_date' : self.advanced_date,
            'due_date' : self.due_date,
            'remitted_date' : self.remitted_date,
            'expected_duration' : self.expected_duration,
            'status' : self.status,
            'insured_invoice' : self.insured_invoice,
            'obligor_notification' : self.obligor_notification,
            'rationale' : self.rationale,
            'late_day' : self.late_day
        }

    def change_rationale(self, new_rationale):
        self.rationale = new_rationale
        Database.update(collection= self.collection, document_id= self.auction_no, data= {"rationale" : new_rationale})

    def change_late_day(self, new_late_day):
        self.late_day = new_late_day
        Database.update(collection=self.collection, document_id=self.auction_no, data={"late_day": new_late_day})

    def change_remitted_day(self, new_remitted_day):
        self.remitted_date = new_remitted_day
        Database.update(collection=self.collection, document_id=self.auction_no, data={"remitted_date": new_remitted_day})



class FInvoice(Invoice):
    def __init__(self, trade_id, requested_loan_amount, expected_tenor, interest_rate, expected_interest_income, buyer,
                 trade_date,actual_repayment_date, actual_tenor, rationale = "Within mandate"):
        super().__init__()
        self.trade_id = trade_id
        self.requested_loan_amount = requested_loan_amount
        self.expected_tenor = expected_tenor
        self.interest_rate = interest_rate
        self.expected_interest_income = expected_interest_income
        self.buyer = buyer
        self.trade_date = trade_date
        self.actual_repayment_date = actual_repayment_date
        self.actual_tenor = actual_tenor
        self.rationale = rationale
        self.collection = "fund_park_invoice"

    def json(self):
        return {
            'id': self.trade_id,
            'trade_id': self.trade_id,
            'requested_loan_amount': self.requested_loan_amount,
            'expected_tenor': self.expected_tenor,
            'interest_rate': self.interest_rate,
            'expected_interest_income': self.expected_interest_income,
            'buyer': self.buyer,
            'trade_date': self.trade_date,
            'actual_repayment_date': self.actual_repayment_date,
            'actual_tenor': self.actual_tenor,
            'rationale': self.rationale
        }

    def change_actual_repayment_date(self, new_actual_repayment_day):
        self.actual_repayment_date = new_actual_repayment_day
        Database.update(collection=self.collection, document_id=self.trade_id,
                        data={"new_actual_repayment_day": new_actual_repayment_day})

    def change_actual_tenor(self, new_actual_tenor):
        self.actual_tenor = new_actual_tenor
        Database.update(collection=self.collection, document_id=self.trade_id,
                        data={"new_actual_repayment_day": new_actual_tenor})

class CInvoice(Invoice):
    def __init__(self, investment_no, obligor, seller, total_investment, return_on_investment, credit_grade, purchase_date,
                 expected_payment_date, unrealized_gain, in_recovery, realized_gain, tenor, rationale = "Within mandate"):
        super().__init__()
        self.collection = "culum_invoice"
        self.investment_no = investment_no
        self.obligor = obligor
        self.seller = seller
        self.total_investment = total_investment
        self.return_on_investment = return_on_investment
        self.credit_grade = credit_grade
        self.purchase_date = purchase_date
        self.expected_payment_date = expected_payment_date
        self.unrealized_gain = unrealized_gain
        self.in_recovery = in_recovery
        self.realized_gain = realized_gain
        self.tenor = tenor
        self.rationale = rationale


    def json(self):
        return {
            'id': self.investment_no,
            'investment_no': self.investment_no,
            'obligor': self.obligor,
            'seller': self.seller,
            'total_investment': self.total_investment,
            'return_on_investment': self.return_on_investment,
            'credit_grade': self.credit_grade,
            'purchase_date': self.purchase_date,
            'expected_payment_date': self.expected_payment_date,
            'unrealized_gain': self.unrealized_gain,
            'in_recovery': self.in_recovery,
            'realized_gain': self.realized_gain,
            'tenor': self.tenor,
            'rationale': self.rationale
        }

class Iinvoice(Invoice):
    def __init__(self, effective_date, transaction_type, invoice, supplier_invoice_number, amount, allocation_amount,
                 allocation_funder_name, trustee_approved, status, discount_rate, expected_repayment_date,
                 financing, credit_insured, external_reference = ""):
        super().__init__()
        self.effective_date = effective_date
        self.transaction_type = transaction_type
        self.invoice = invoice
        self.supplier_invoice_number = supplier_invoice_number
        self.amount = amount
        self.allocation_amount = allocation_amount
        self.allocation_funder_name = allocation_funder_name
        self.trustee_approved = trustee_approved
        self.status = status
        self.discount_rate = discount_rate
        self.expected_repayment_date = expected_repayment_date
        self.financing = financing
        self.credit_insured = credit_insured
        self.external_reference = external_reference

    def json(self):
        return {
            'id': self.supplier_invoice_number,
            'effective_date': self.effective_date,
            'transaction_type': self.transaction_type,
            'invoice': self.invoice,
            'supplier_invoice_number': self.supplier_invoice_number,
            'amount': self.amount,
            'allocation_amount' : self.allocation_amount,
            'allocation_funder_name' : self.allocation_funder_name,
            'trustee_approved': self.trustee_approved,
            'status': self.status,
            'discount_rate': self.discount_rate,
            'expected_repayment_date': self.expected_repayment_date,
            'financing': self.financing,
            'credit_insured': self.credit_insured,
            'external_reference': self.external_reference
        }













