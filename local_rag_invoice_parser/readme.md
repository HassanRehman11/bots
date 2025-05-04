# Invoice Data Extractor 📄

A command-line tool that extracts structured invoice data from PDF documents (in German or English) and outputs the results in XML format. Utilizes Ollama's `deepseek-r1:8b` model for embeddings and question-answering, along with LangChain for document loading, splitting, indexing, and retrieval.

## Features

* **PDF Loading**: Uses `PDFPlumberLoader` to read PDF invoices.
* **Text Splitting**: Splits documents into manageable chunks with `RecursiveCharacterTextSplitter`.
* **Vector Store**: Stores embeddings in an in-memory vector store for similarity search.
* **Embeddings & Model**: Leverages Ollama's `deepseek-r1:8b` for embeddings (`OllamaEmbeddings`) and querying (`OllamaLLM`).
* **Structured Extraction**: Retrieves relevant text chunks and generates XML-formatted invoice data, preserving original language and formatting.
* **Command-Line Interface**: Specify input PDF and output directory via arguments.

## Data Structure

The extracted XML follows this structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Invoice>
  <Sender>
    <Name>...</Name>
    <Address>...</Address>
    <Contact>
      <Phone>...</Phone>
      <Fax>...</Fax>
      <Website>...</Website>
    </Contact>
    <BankDetails>
      <BankName>...</BankName>
      <IBAN>...</IBAN>
      <SWIFTBIC>...</SWIFTBIC>
      <USTID>...</USTID>
    </BankDetails>
  </Sender>
  <Receiver>
    <Name>...</Name>
    <Address>...</Address>
  </Receiver>
  <OrderDetails>
    <CustomerNumber>...</CustomerNumber>
    <OrderDate>DD.MM.YYYY</OrderDate>
    <OrderNumber>...</OrderNumber>
    <InvoiceDate>DD.MM.YYYY</InvoiceDate>
    <InvoiceNumber>...</InvoiceNumber>
    <Items>
      <Item>
        <Position>...</Position>
        <ArticleNumber>...</ArticleNumber>
        <Description>...</Description>
        <Quantity>...</Quantity>
        <UnitPriceEUR>...</UnitPriceEUR>
        <TotalPriceEUR>...</TotalPriceEUR>
        <VATPercent>...</VATPercent>
      </Item>
      <!-- More items -->
    </Items>
    <TotalAmount>
      <NetAmountEUR>...</NetAmountEUR>
      <VATAmountEUR>...</VATAmountEUR>
      <GrossAmountEUR>...</GrossAmountEUR>
    </TotalAmount>
  </OrderDetails>
  <PaymentDetails>
    <PaidAt>...</PaidAt>
    <ReceiptOrderNumber>...</ReceiptOrderNumber>
  </PaymentDetails>
</Invoice>
```

## Requirements

* Python 3.8+
* [ollama](https://ollama.com/) (CLI installed and model `deepseek-r1:8b` available)
* Python packages:

  * `langchain-community`
  * `langchain-text-splitters`
  * `langchain-core`
  * `langchain-ollama`
  * `ollama`

Install with:

```bash
pip install langchain-community langchain-text-splitters langchain-core langchain-ollama ollama
```

## Usage

1. Ensure Ollama model is available:

   ```bash
   ollama show "deepseek-r1:8b" || ollama pull "deepseek-r1:8b"
   ```

2. Run the extractor:

   ```bash
   python invoice_extractor.py -i /path/to/invoice.pdf -o /path/to/output_dir
   ```

3. The XML file will be saved in the output directory with the same base name as the PDF.

## Development

* The main script `invoice_extractor.py` defines functions for loading, splitting, indexing, retrieving, and answering.
* Modify the `question` template in the script to adjust extraction rules.

