export default function DocumentDetailsModal({
  document,
  onClose
}) {
  if (!document) return null;
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white w-[90%] max-w-4xl rounded-2xl p-8 max-h-[90vh] overflow-y-auto">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-3xl font-bold">Document Details</h2>
          <button
            onClick={onClose}
            className="bg-red-500 text-white px-4 py-2 rounded-lg">
            Close
          </button>
        </div>
        <div className="grid grid-cols-2 gap-6 mb-8">
          <div>
            <h3 className="font-bold text-gray-500">File Name</h3>
            <p>{document.file_name}</p>
          </div>
          <div>
            <h3 className="font-bold text-gray-500">Upload Date</h3>
            <p>{document.upload_date}</p>
          </div>
          <div>
            <h3 className="font-bold text-gray-500">OCR Status</h3>
            <p>{document.ocr_status}</p>
          </div>
          <div>
            <h3 className="font-bold text-gray-500">Validation Status</h3>
            <p>{document.validation_status}</p>
          </div>
        </div>
        <div className="mb-8">
          <h2 className="text-2xl font-bold mb-4">Extracted Invoice Data</h2>
          <div className="grid grid-cols-2 gap-6">
            <div>
              <h3 className="font-semibold">Invoice Number</h3>
              <p>{document.invoice_number}</p>
            </div>
            <div>
              <h3 className="font-semibold">Buyer Name</h3>
              <p>{document.buyer_name}</p>
            </div>
            <div>
              <h3 className="font-semibold">Seller Name</h3>
              <p>{document.seller_name}</p>
            </div>
            <div>
              <h3 className="font-semibold">Country</h3>
              <p>{document.country}</p>
            </div>
            <div>
              <h3 className="font-semibold">Product</h3>
              <p>{document.product}</p>
            </div>
            <div>
              <h3 className="font-semibold">Quantity</h3>
              <p>{document.quantity}</p>
            </div>
            <div>
              <h3 className="font-semibold"> Price</h3>
              <p>{document.currency} {document.unit_price}</p>
            </div>
          </div>
        </div>
        <div>
          <h2 className="text-2xl font-bold mb-4">n
            Raw OCR Text
          </h2>
          <div className="bg-gray-100 p-4 rounded-xl whitespace-pre-wrap">
            {document.raw_text}
          </div>
        </div>
      </div>
    </div>
  );
}