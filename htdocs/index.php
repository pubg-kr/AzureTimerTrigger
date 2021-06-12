<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>코로나 확진자</title>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>

<body>
<table width="993" height="319" border="3">
<?php
		
		require_once 'vendor/autoload.php';

		use MicrosoftAzure\Storage\Table\TableRestProxy;
		use MicrosoftAzure\Storage\Common\Exceptions\ServiceException;

		$connectionString = "DefaultEndpointsProtocol=[http|https];AccountName=[hotblobstorage1324];AccountKey=[ObDu0ST/O2vwNnsY9yr4DSctTXmdza0inVo6IaGxwKv0l5KkUuFeE0Xkm94xG3GKkDOVtmndS0mfWPD6vm9elQ==]";
		$tableClient = TableRestProxy::createTableService($connectionString);

		try    {
		$result = $tableClient->getEntity("coronaTable", "corona_index", 1);
		}
		catch(ServiceException $e){
		
		$code = $e->getCode();
		$error_message = $e->getMessage();
		echo $code.": ".$error_message."<br />";
		}

		$seoul = $result->getEntity("seoul");
		$ulsan = $result->getEntity("ulsan");
		$daegu = $result->getEntity("daegu");
		$gwangju = $result->getEntity("gwangju");
		$busan = $result->getEntity("busan");
		$daejeon = $result->getEntity("daejeon");
		$incheon = $result->getEntity("incheon");
	
		$seoulNew = $result->getEntity("seoulNew");
		$ulsanNew = $result->getEntity("ulsanNew");
		$daeguNew = $result->getEntity("daeguNew");
		$gwangjuNew = $result->getEntity("gwangjuNew");
		$busanNew = $result->getEntity("busanNew");
		$daejeonNew = $result->getEntity("daejeonNew");
		$incheonNew = $result->getEntity("incheonNew");

		$total = $seoul +$ulsan + $daegu + $gwangju + $busan + $daejeon + $incheon;
		$newTotal = $seoulNew +$ulsanNew + $daeguNew + $gwangjuNew + $busanNew + $daejeonNew + $incheonNew;


				echo (
					'  <tr>
							<th width="18" scope="col">지역</th>
							<th width="54" scope="col">누적 확진자(명)</th>
							<th width="54" scope="col">신규 확진자(명)</th>
						 </tr>'			
				);
?>
                <tr>
                    <td>서울 </td>
                    <td><?= $seoul?> </td>  
					<td><?= $seoulNew?> </td>                    
                </tr>
				<tr>
                    <td>울산 </td>
                    <td><?=$ulsan ?> </td>        
					<td><?=$ulsanNew ?> </td>                    
            
                </tr>
				<tr>
                    <td>대구 </td>
                    <td><?=$daegu?> </td>    
					<td><?=$daeguNew?> </td>                    
                
                </tr>
				<tr>
                    <td>광주 </td>
                    <td><?=$gwangju ?> </td>     
					<td><?=$gwangjuNew ?> </td>                    
               
                </tr>
				<tr>
                    <td>부산</td>
                    <td><?=$busan?> </td> 
					<td><?=$busanNew?> </td>                    
                   
                </tr>
				<tr>
                    <td>대전 </td>
                    <td><?=$daejeon?> </td>  
					<td><?=$daejeonNew?> </td>                    
                  
                </tr>
				<tr>
                    <td>인천 </td>
                    <td><?=$incheon?> </td>          
					<td><?=$incheonNew?> </td>                    
          
                </tr>		
				<tr>
                    <td>합계 </td>
                    <td><?=$total?> </td>          
					<td><?=$newTotal?> </td>                    
          
                </tr>

</table>

</body>
</html>
